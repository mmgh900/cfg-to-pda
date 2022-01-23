# What is it?
##Language and machine theory lesson project
Implementing a text-to-PDA algorithm In this project you need to implement a text-to-PDA algorithm. The program you write for this project should include the following 3 features.
Getting grammar from the user: Your application should be able to get grammar independent of the text from the user. The grammar has the same form as read in the lesson. For example, the following is an example grammar that the user should be able to enter in the system:

`S -> aSb | aSbb | A`
`A -> aA | λ`

Use the λ symbol as Landa
Read grammar processing: Your application must process the user-derived grammar, break it down into smaller parts, and generate PDA transfer functions corresponding to the grammar. The rules produced must have the same form as taught in the classroom.
Generating a PDA using Transfer Functions: Finally, you must create the corresponding PDA corresponding to the language using the conversion functions generated in the previous step. To do this, you must create a class for states in which the states to which they go are specified along with the transfer function. Also if this state the start or end node must be specified with a Flag.
Finally, your application should be able to take a string and, after reviewing it and inserting it into the PDA, confirm or deny its membership in the language corresponding to the PDA.
You can use JAVA, CPP #, C, Python to code this project.

## Additional explanations:
The project must be object-oriented.

You must submit all the code you entered for the project in a zip file.

Any ambiguous part of this project can be identified and defined by you if it is logical.

Upon delivery, complete mastery of the submitted code and the ability to change it at the project level is required.


# How to run
Follow these steps:
1. Run `python main.py` on your machine
2. Enter the number of grammar rules you want to enter
3. Enter grammar rules
4. Enter a candidate string to be passed

Note: The start variable of your grammar will be determined by the first symbol that you enter in your grammar rules