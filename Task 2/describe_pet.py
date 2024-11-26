def describe_pet(**args):
    for k, v in args.items():
        print(f"{k} = {v}")


describe_pet(Name='Barsik', Age=5, Sex='Male', Color="Black")
