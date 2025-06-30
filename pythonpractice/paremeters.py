

def Patient(name,BloodGroup,*diseases,email_id=None):
    print(f"name:{name}")
    print(f"Blood group:{BloodGroup}")
    print(f"diseases:{diseases}")
    print(f"email_id: {email_id if email_id else 'Not provided'}")
    print("-" * 30)


Patient("bhagya","b-positive","fever",email_id= "bhagya@example.com")


