# Created by:- Wasim

# importing modules
import boto3

# Initialize IAM client
aws_console = boto3.session.Session(profile_name= "default")
iam_console = aws_console.client("iam")


def delete_user(user_name, policy_arns):
# Detach policies from the user
    for policy_arn in policy_arns:

        try:
            iam_console.detach_user_policy(
                UserName=user_name,
                PolicyArn=policy_arn,
            )

            print(f"Successfully detached policy for User {user_name}")

        except iam_console.exceptions.NoSuchEntityException: 
            print(f"Error: Policy {policy_arns} or user {user_name} does not exist.")
        
        except Exception as e:
            print("An unexpected error ocure while detaching policy")

# Delete the user login profile
    try:

        iam_console.delete_login_profile(
            UserName= user_name,
        )

        print(f"Successfully deleted login profile for user {user_name}.")

    except iam_console.exceptions.NoSuchEntityException:
        print(f"Error: No login profile exists for user {user_name}.")

    except Exception as e:
        print("An unexpected error ocure while deleting loging profile")

# Delete the user
    try:

        iam_console.delete_user(
            UserName=user_name,
        )

        print(f"Successfully deleted user {user_name}.")

    except iam_console.exceptions.NoSuchEntityException:
        print(f"Error: User {user_name} does not exist.")
    
    except Exception as e:
        print(f"An unexpected error occurred while deleting the user: {e}")



user_name = input("Enter the username: ")

# Policies set for my user [your can be diffrent]
policy_arns = [ 
    'arn:aws:iam::864981749658:policy/IAMUserManagementPolicy', 
    'arn:aws:iam::aws:policy/AmazonEC2FullAccess', 
]

delete_user(user_name, policy_arns)