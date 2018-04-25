### IMPORTANT: Your program must run on Python 3.6.4
### No libraries may be used unless explicitly
### authorized by instructor via email


### Rename file by adding your last name to the file name:
### instead of InputFile318Skeleton.py call it
### InputFile318MyName.py. For examle: InputFile318Munoz.py

### Last update: 4/18/2018 at 10:40AM

#####################################
### DFA
#####################################

MyName = 'Put your name here' ## please put your name here
FunctionsIworkedOn = {'verifyDFA', 'verifyTM'} ## List all functions you are submitting here
### Any function you are not submitting for grading please leave
### it unmodified, as it was originally in this file. DO NOT DELETE IT

class DFA(object):
    def __init__(self, Q=None, Sigma=None, Delta=None, q0=None, F=None):
        self.Q = Q
        self.Sigma = Sigma
        self.Delta = Delta
        self.q0 = q0
        self.F = F

    def verifyDFA(self):
         # Decides if self is a correct DFA
         # Verification needs to be extended.
         # DO NOT change the input representation of DFAs

        for k,v in self.Delta.items():
             if not k in self.Q:
                print ("error:", k, self.Q)
                return False # transition from a non-state
             for k1,v1 in v.items():
               if not k1 in self.Sigma:
                   print ("error:", k1, self.Sigma)
                   return False # transition with a symbol not in Sigma
               if not v1 in self.Q:
                   print ("error:", v1, self.Q)
                   return False  # transition to a non-state
               
        # Add code verifying that each state in Q has one and only one transtion
        # in Delta for each symbol in Sigma.
        # If so return True; otherwise return False

        return True    
       

    def acceptDFA(self,s):
        # Decides if self  accepts s
       
        return True
        

    def emptyDFA(self):
        # Decides if self  accepts no  strings
        
       return True

    def EQDFA(self,D):
       # Decides if L(self) = L(D), where D is a DFA

        return True



#####################################
### PDA 
#####################################

class PDA(object):
    def __init__(self, Q=None, Sigma=None, Gamma=None, Delta=None, q0=None, F=None):
        self.Q = Q
        self.Sigma = Sigma # may not contain 'e', which we use to denote the empty string
        self.Gamma = Gamma # may not contain 'e', which we use to denote the empty string
        self.Delta = Delta # may use 'e', which we use to denote the empty string
        self.q0 = q0
        self.F = F

    def verifyPDA(self):
         # Decides if self is a correct PDA
         # 'e' denotes the empty string 
         # DO NOT change the input representation of PDAs
        
        
         return True

    def acceptPDA(self,s):
        # Decides if self accepts s with at most 2|s| transitions from the start state
        # Must try all possible transitions 
        return True

    def notEQPDA(self,P,k):
        # Quasi-ecognizes if L(self) != L(P), where P is a  PDA
        # try all strings of length  0, 1, 2, .., k.
        # When it reaches strings of length  k+1, it returns false.
        # A true recognizer would not stop at k and simply continue running.
        # We add k so it always terminate
        
        return True  
               
        
#####################################
### TM 
#####################################

class TM(object):
    def __init__(self, Q=None, Sigma=None, Gamma=None, Delta=None, q0=None, qAccept=None, qReject=None):
        self.Q = Q
        self.Sigma = Sigma
        self.Gamma = Gamma # '_' is the blank symbol
        self.Delta = Delta # Move to left: 'L'; move to right: 'R'
        self.q0 = q0
        self.qAccept = qAccept
        self.qReject = qReject

    def verifyTM(self):
        # Decides if self is a correct TM
        # Verification needs to be extended.
        # '_' is the blank symbol
        # DO NOT change the representation of TM
        
        for k,v in self.Delta.items():
            if not k in self.Q:
               print ("error:", k, self.Q) 
               return False  # transition from a non-state
            for k1,v1 in v.items():
               if not k1 in self.Gamma:
                   print ("error:", k1, self.Sigma)
                   return False # transition reading a symbol not in Gamma
               if not v1[0] in self.Q:
                   print ("error:", v1[0], self.Q)
                   return False # transition to  a non-state
               if not v1[1] in self.Gamma:
                   print ("error:", v1[1], self.Gamma)
                   return False # transition writing a symbol not in Gamma
               if not v1[2] in ['L','R']:
                   print ("error:", v1[2], "should be L or R")
                   return False # "should be L or R"
            

        # Add code verifying that each state in Q has one and only one transtion
        # in Delta for each symbol in Gamma.
        # If so return True; otherwise return False

        return True    
       
    def acceptTM(self,s,k):
        # Quasi-recognizes if TM self accepts s
        # if TM reaches an accepting state, it should accept
        # if TM reaches a rejecting states it should reject.
        # '_' is the blank symbol
        # s is a list; it is used as the initial tape;
        # assumes head pointing to first symbol in s
        # returns false if the number of transitions exceeds k.
        # A true recognizer would not stop at k and simply continue running.
        # We add k so it always terminate
        
        head = 0
        
        return True
        
            
#####################################
### NTM 
#####################################

class NTM(object):
    def __init__(self, Q=None, Sigma=None, Gamma=None, Delta=None, q0=None, qAccept=None):
        self.Q = Q
        self.Sigma = Sigma
        self.Gamma = Gamma # '_' is the blank symbol
        self.Delta = Delta # Move to left: 'L'; move to right: 'R'
        self.q0 = q0
        self.qAccept = qAccept
      

    def verifyNTM(self):
        # Decides if self is a correct NTM
        # '_' is the blank symbol
        # DO NOT change the representation of NTM
        
        return True    
       
    def acceptNTM(self,s,k):
        # Quasi-recognizes if NTM self accepts s; NTM has no reject state
        # s is a list; it is used as the initial tape;
        # assumes head pointing to first symbol in s
        # If it doesn't reach an accepting state with all transitions of lenght k, return false.
        # A true recognizer would not stop at k and simply continue running.
        # We add k so it always terminate
        
        head = 0
        
        return True
        

