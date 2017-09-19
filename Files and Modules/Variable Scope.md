When you program, you'll often find that similar ideas come up again and again. You'll use variables for things like counting, iterating and accumulating values to return. 
In order to write readable code, you'll find yourself wanting to use similar names for similar ideas. As soon as you put multiple piece of code together (for instance, multiple functions or function calls in a single script) you might find that you want to use the same name for two separate concepts.

Fortunately, you don't need to come up with new names endlessly. Reusing names for objects is OK as long as you keep them in separate scope. "Scope" refers to which parts of a program a variable can be referenced from.

If a variable is created inside a function, it can only be used within that function.

Consider these two functions, word_count and nearest_square. Both functions include a answer variable, but they are distinct variables that only exist within their respective functions.

    def word_count(document, search_term):
        """ Count how many times search_term appears in document. """
        words = document.split()    
        answer = 0
        for word in words:
            if word == search_term:
                answer += 1
        return answer

    def nearest_square(limit):
        """ Find the largest square number smaller than limit. """
        answer = 0
        while (answer+1)**2 < limit:
            answer += 1
        return answer**2        

It's best to define variables in the smallest scope they will be needed in. While functions can refer to variables defined in a larger scope, this is very rarely a good idea.

   