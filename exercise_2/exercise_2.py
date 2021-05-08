def exercise_2(inputs): # DO NOT CHANGE THIS LINE
    #EXERCISE_2

    class Party():
        def __init__(self):
            self.info_attendees = {}
            self.detailed_info_attendees = {}

        def add_attendees(self,family_names,number_of_attendees):
            l=0
            for k in family_names:
                self.info_attendees[k]=number_of_attendees[l]
                l=l+1

        def detailed_attendees(self,family_names,adult_attendees,child_attendees):
            o=0
            for d in family_names:
                self.detailed_info_attendees[d]=[adult_attendees[o],child_attendees[o]]
                o=o+1

        def check_and_resolve(self):
            for e in self.info_attendees:
                if self.info_attendees.get(e)==(self.detailed_info_attendees.get(e)[0]+self.detailed_info_attendees.get(e)[1]):
                    pass
                else:
                    print("information do not match for",e,"family, the input of total number of attendees does not match with the total number of adults and child attendees")

        def get_total_attendees(self):
            c=0
            for f in self.info_attendees:
                c=c+self.info_attendees.get(f)

        def filter_attendees(self):
            for g in self.detailed_info_attendees:
                if (self.detailed_info_attendees.get(g)[0]+self.detailed_info_attendees.get(g)[1])>2 or self.detailed_info_attendees.get(g)[1]>0:
                    return g
                else:
                    pass

        def covid_changes(self):
            for p in self.info_attendees:
                if (self.detailed_info_attendees.get(p)[0]+self.detailed_info_attendees.get(p)[1])>2 or self.detailed_info_attendees.get(p)[1]>0:
                    print("Dear Mr/Mrs",p+",","due to the covid-19 situation, you are only allowed to bring up to 2 adult family members and you cannot bring any children to the party")
                else:
                    pass

        def include_priority(self,priorities):
            z=0
            for i in self.detailed_info_attendees:
                self.detailed_info_attendees[i]=self.detailed_info_attendees.get(i)+[priorities[z]]
                z=z+1

        def filter_priorities(self):
            for j in self.detailed_info_attendees:
                if self.detailed_info_attendees.get(j)[2]<=priority:
                    return j

    #INPUT EXAMPLE

    #familynames=["Lee","Loa","Parker"]
    #numberofattendees=[3,5,3]
    #adultattendees=[2,3,3]
    #childattendees=[1,2,0]
    #prioritiess=[1,3,5]
    #priority=3

    #OUTPUT EXAMPLE

    #p=Party()
    #p.add_attendees(familynames, numberofattendees)
    #p.detailed_attendees(familynames, adultattendees, childattendees)
    #p.check_and_resolve()
    #p.get_total_attendees()
    #p.filter_attendees()
    #p.include_priority(prioritiess)
    #p.filter_priorities()
    
    output = [Party]

    return output       # DO NOT CHANGE THIS LINE
