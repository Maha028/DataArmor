import pandas as pd
class mondrian:
    '''
        Class implements the recursive partition of data in size at least k,
        anonymizes the Explicit IDs, and checks each partition if it achieves
        k-anonymity when combining QIDs if not it will anonymize the QIDs 
        (ordered by the diversity of its values) until it achive k-anonymity in
        each partition
    '''
        
        
    def __init__(self,csv_data,EID,cat_qid,num_qid,k):
        
        self.csv_data=csv_data
        self.data=pd.read_csv(f"{self.csv_data}")#create data frame from csv file to easly handle data
        '''Functions Calls when object created'''
        
        self.variable_init(cat_qid,num_qid,k,EID)
    
        self.choose_quasi_identifier()
        self.result_partitions=self.k_partition(self.data,self.qid[0]) #partition data based on first qi that have the most diversity
        #self.calculate_k()
        if self.EID:
            self.mask_explicit_att()
        
        self.anonymize_partitions()

        #self.save_in_csv_file()#last function call

        
    def variable_init(self,cat_qid,num_qid,k,EID):
        
        ''' initiate required variables '''
        
        self.k=k-1  #k = min{|P_x|: x âˆˆ T}
        self.num_qid=num_qid
        self.cat_qid=cat_qid
        self.qid=self.num_qid+self.cat_qid
        self.EID=EID

    '''
    def calculate_k(self):
        df=self.data
        k=[]
        x=0
        for i in self.qid: 
            k.append(5000)
            for partition in self.result_partitions:
                for j in partition[i]:
                    if df[df[i] == j].shape[0]< k[x]:
                        k[x]=df[df[i] == j].shape[0]
            x+=1
        self.kb=[]
        k.sort()
            
        self.kb.append(f"k value of QIDs combination: {k[0]}")
        
        for i in range(len(self.qid)):
            self.kb.append(f"k value of {self.qid[i]} column : {k[i] }")
    '''
    def choose_quasi_identifier(self):
        
        '''rearrange quasi-identifiers descending based on their values diversity and uniqueness '''
        
        diversit=[]
        for qi in self.qid:
            diversity = self.data[qi].nunique()  # Calculate the number of unique values for the quasi-identifier
            diversit.append(diversity)
        
        for i in range(len(diversit)-1):
            if diversit[i]<diversit[i+1]:
                temp=self.qid[i]
                self.qid[i]=self.qid[i+1]
                self.qid[i+1]=temp

    def k_partition(self,data,qi):
        
        '''' Function returns the data partitioned into at least k-sized partition '''

        partitions= []
        
        if(len(data)<=(2*self.k-1)): #if it splitabile or not (2*k-1)
            partitions.append(data)
            return [data]
        so=sorted(self.qid, reverse=True)
        data = data.sort_values(by=so)
        si=data[qi].count()
        mid = si//2
        
        lhs= data[:mid]
        rhs= data[mid:]
        partitions.extend(self.k_partition(lhs,qi))
        partitions.extend(self.k_partition(rhs,qi))
        return partitions
    
    
    def mask_explicit_att(self):
        for partition in self.result_partitions:
            for i in self.EID:
                self.mask_non_numeric(partition,i)
        
            
            
    def count_qi_combinations(self, partition,  quasi_identifiers):
        
        '''
        Count the number of distinct quasi-identifier combinations in a partition. to ensure that this partition
        satisfies k-anonymity when combining all quasi-identifiers or not 
        '''
        qi_combinations = set()
        for index, row in partition.iterrows():
            qi_values = tuple(row[i] for i in  quasi_identifiers)
            qi_combinations.add(qi_values)           
        return len(qi_combinations)
    
    def count_qi(self, m, partition ,qi):
        
        '''
        Count the number of distinct quasi-identifier combinations in a partition. to ensure that this partition
        satisfies k-anonymity when combining all quasi-identifiers or not 
        '''
        df=m
        qi_combinations = set()
        for index, row in partition.iterrows():
            qi_values = tuple(row[i] for i in  qi)
            qi_combinations.add(qi_values) 
        qi_combinations=[list(item) for item in qi_combinations]
        
        for i in qi_combinations:
            if (df[(df[qi[0]] == i[0]) & (df[qi[1]] == i[1]) & (df[qi[2]] == i[2])].shape[0] >=self.k):
                return 1
        return 0
    def anonymize_partitions(self):
        ''' 
        check if the partition satisfies k-anonymity if not will 
        anonymize the quasi-identifiers until k-anonymity achived
        '''
        
        qi=self.qid
        for i in range(len(qi)):#[age,country,gender]
            self.m=pd.concat(self.result_partitions,ignore_index=True)
            for partition in self.result_partitions:
                #self.mask_non_numeric(partition, self.EID)
                
                if self.count_qi_combinations(partition, qi)==1:
                    continue
                else:
                    if qi[i] in self.num_qid:
                        partition=self.genrlize_numirical(partition, qi[i])
                    else:
                        partition=self.mask_non_numeric(partition,qi[i])


    def genrlize_numirical(self,partition,num_qid):#not completed
            min=self.data[num_qid].min()
            max=self.data[num_qid].max()
            mid=(min+max)//2
            for i in partition[num_qid]:
                if i>=mid:
                    gen=f">={mid}"
                    partition[num_qid]=gen
                else:
                    gen=f"<{mid}"
                    partition[num_qid]=gen
                    
            return partition
    
    def mask_non_numeric (self,partition,cat_qi):
    
        partition=partition    
        gen ="*****"
        partition[cat_qi]=gen
        
        if (len(partition)<self.k):
            print("error")
        
        return partition
    
    def save_in_csv_file(self):
        #-----------save result to csv file--------------------------------
        anonymization_data=pd.concat(self.result_partitions,ignore_index=True)
        anonymization_data=anonymization_data.sort_index()
        anonymization_data.to_csv('anonymized_data.csv',index=False)
'''
k = 4
EID=["name"]
num_qid=["age"]
cat_qid=["gender","country"]
mondrian("data1.csv", EID,cat_qid, num_qid, k)'''