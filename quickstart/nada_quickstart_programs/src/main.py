from nada_dsl import *


def nada_main():
    devansh = Party(name="Devansh")  
    prathamesh = Party(name="Prathamesh")  
    abhishekh = Party(name="Abhishekh")  

    devansh_salary = SecretInteger(Input(name="devansh_salary", party=devansh))
    prathamesh_salary = SecretInteger(Input(name="prathamesh_salary", party=prathamesh))
    abhishekh_salary = SecretInteger(Input(name="abhishekh_salary", party=abhishekh))
   
    lowest_position = (devansh_salary < prathamesh_salary).if_else(
        (devansh_salary < abhishekh_salary).if_else(Integer(0), Integer(2)),
        (prathamesh_salary < abhishekh_salary).if_else(Integer(1), Integer(2)),
    ) 
    devansh_prathamesh_tie = (devansh_salary == prathamesh_salary)
    prathamesh_abhishekh_tie = (prathamesh_salary == abhishekh_salary)
    devansh_abhishekh_tie = (devansh_salary == abhishekh_salary)
    
    complex_lowest_position = devansh_prathamesh_tie.if_else(
        prathamesh_abhishekh_tie.if_else(
            Integer(0),  
            (devansh_salary < abhishekh_salary).if_else(Integer(0), Integer(2))  
        ),
        
        prathamesh_abhishekh_tie.if_else(
            (prathamesh_salary < devansh_salary).if_else(Integer(1), Integer(0)),  
            devansh_abhishekh_tie.if_else(
                (devansh_salary < prathamesh_salary).if_else(Integer(0), Integer(1)),  
                lowest_position  
            )
        )
    )
    out = Output(complex_lowest_position, "lowest_position", devansh)

    return [out]
