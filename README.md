#  Email Slicer (Python)

A beginner-friendly Python project that validates an email address and extracts (slices) the **username** and **domain name** from it.

This project is useful for learning:
- String handling in Python
- Input validation
- Loops and conditions
- Regular Expressions (Regex)

---

##  Project Idea

The Email Slicer is a handy program that:
1. Takes an email address from the user  
2. Validates it using rules  
3. Extracts the **username** and **domain name**  
4. Displays the result in a clean format  

---

##  Features

- Checks that the email contains exactly **one `@`**
- Prevents `@` from being at the start or end
- Rejects emails containing spaces
- Ensures the domain contains a valid `.` format
- Prevents consecutive dots (`..`) in username or domain
- Ensures username contains only valid characters using **Regex**
- Allows only `.com`, `.org`, `.net` extensions



##  Validation Rules Used

The program checks:

 Email must not contain spaces  
 Email must contain exactly one `@`  
'@' cannot be at the start or end  
 Username cannot be empty  
 Domain name cannot be empty  
 Domain must contain '.' 
 Domain cannot start/end with '.'  
 Username cannot start/end with '.'  
 Username and domain cannot contain '..'  
 Username must match
   Domain extension must be:
  '.com'
  '.org'
  '.net'


