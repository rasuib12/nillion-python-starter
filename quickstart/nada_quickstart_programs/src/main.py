from nada_dsl import *


def nada_main():
    devansh = Party(name="Devansh")  # party 0
    prathamesh = Party(name="Prathamesh")  # party 1
    abhishekh = Party(name="Abhishekh")  # party 2

    devansh_salary = SecretInteger(Input(name="devansh_salary", party=devansh))
    prathamesh_salary = SecretInteger(Input(name="prathamesh_salary", party=prathamesh))
    abhishekh_salary = SecretInteger(Input(name="abhishekh_salary", party=abhishekh))

    # Determine the lowest position
    lowest_position = (devansh_salary < prathamesh_salary).if_else(
        (devansh_salary < abhishekh_salary).if_else(Integer(0), Integer(2)),
        (prathamesh_salary < abhishekh_salary).if_else(Integer(1), Integer(2)),
    )

    # Adding complexity: Check for ties
    devansh_prathamesh_tie = (devansh_salary == prathamesh_salary)
    prathamesh_abhishekh_tie = (prathamesh_salary == abhishekh_salary)
    devansh_abhishekh_tie = (devansh_salary == abhishekh_salary)

    # Create a more complex condition with tie checks
    complex_lowest_position = devansh_prathamesh_tie.if_else(
        prathamesh_abhishekh_tie.if_else(
            Integer(0),  # All three salaries are equal
            (devansh_salary < abhishekh_salary).if_else(Integer(0), Integer(2))  # Devansh and Prathamesh are equal, compare with Abhishekh
        ),
        prathamesh_abhishekh_tie.if_else(
            (prathamesh_salary < devansh_salary).if_else(Integer(1), Integer(0)),  # Prathamesh and Abhishekh are equal, compare with Devansh
            devansh_abhishekh_tie.if_else(
                (devansh_salary < prathamesh_salary).if_else(Integer(0), Integer(1)),  # Devansh and Abhishekh are equal, compare with Prathamesh
                lowest_position  # No ties, use the original lowest position
            )
        )
    )

    out = Output(complex_lowest_position, "lowest_position", devansh)

    return [out]
