while True:
  try:
     a = int(input("Enter the length of the  (1-6): "))
  except ValueError:
     continue
  else:
    if a in arr:
     print("Variant is available!")
     break
    else:
     print("Variant is not 1-6!")