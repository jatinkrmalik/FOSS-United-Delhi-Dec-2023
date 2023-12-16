%title: FOSS United Delhi / Dec 23
%author: @jatinkrmalik
%date: 2023-12-16

-> # The Coder's Guide to Job Security <-

^

-> *Mastering the Art of Confusing Code!* <- 

^

-> > Jatin K Malik <-

---

-> # A quick intro?! <-

`res/intro_jatin.png`

`res/hobbies_jatin.png`

---

Let's get started?!

---

> Quidquid latine dictum sit, altum sonatur.

^

- Whatever is said in Latin sounds **profound**.

---

In the interests of creating employment opportunities in the Backend, I am passing on these tips from the masters on how to write code that is so **difficult** to maintain, that the people who come after you will take **years** to make even the simplest changes.
^

Further, if you follow all these rules religiously, you will even guarantee yourself a **lifetime of employment**, since no one but you has a hope in hell of maintaining the code. 

---

Then again, if you followed all these rules religiously, **even you** wouldn't be able to maintain the code!
^

> You **don't** want to overdo this. Your code should not look hopelessly unmaintainable, just be that way. 
^

-> *Otherwise it stands the risk of being rewritten or refactored.* <-

---

-> # General Principles <-

To foil the **KTLO** programmer, you have to understand how they think.

- They have your giant program. 
- They have no time to read it all, much less understand it. 
^

> They want to **rapidly find** the place to make his change, **make** it and **get out** and have **no unexpected side effects** from the change.

---

- Programmers are lulled into complacency by **conventions**. By every once in a while, by subtly **violating** convention, you force him to read *every line of your code with a magnifying glass*.
^

- You might get the idea that every language feature makes code **unmaintainable** -- not so, only if properly misused.

---

-> `src/0_naming_conventions.py` <-

- Much of the skill in writing unmaintainable code is the art of **naming variables and methods**. They **don't matter** at all to the compiler.

- Keep them **guessing** what each variable and function does!
^

- This is just a **simple factorial function**, but the naming conventions make it look like a complex space travel simulation.

---

-> Protip: **A.C.R.O.N.Y.M.S.** <-
^
- Use acronyms to keep the code terse. 
^
- Real programmers never define acronyms; they understand them genetically.

---

> Incorrect documentation is often worse than no documentation.
  
Since the computer **ignores** comments and documentation, you can **lie outrageously** and do everything in your power to befuddle the poor maintenance programmer.

---

-> `src/1_documentation.py` <-

- Provide **general and unhelpful comments** like `Data transformation phase 1` and `Final output preparation`.

- **Avoid** explaining the purpose behind specific operations or logic.

- Use comments to give a **false sense of understanding**, while the actual code remains cryptic.

---

-> `src/2_code_structure.py` <-

- Nest conditions like **Russian dolls**
  
- Good coders can get up to **10 levels** of ( ) on a single line and **20 { }** in a single method
  
- The **deeper**, the **better**.

---


-> `src/3_inconsistent_style.py` <-

- Mix **camelCase** and **snake_case** in function and variable names.
  
- Use **inconsistent capitalization** in class and method names.
  
- Combine **different naming conventions** within the same code block, making it hard to follow a consistent style.

---


-> `src/4_magic_numbers.py` <-

- Use numbers like `42, 17, 23, 13, 3.14, 2.718` without any explanation.

- Integrate these **magic numbers** into complex calculations. Why use constants when you can keep them **mystified**?

---

> Always look for the most obscure way to do common tasks!

---


-> `src/5_can_you_spot_the_obfuscation.py` <-

- Examine the **private nested function** applying **bitwise** operations.
  
- Focus on how the string undergoes **transformation** and then another operation.

---

- Well, it's not that hard to figure out what this code does, but it's still confusing enough to make you wonder why it's written this way.
  
- The complexity disguises a **simple yet common** string operation.

`result = input_str[::-1]`

---

-> `src/6_overcomplicate_simple_tasks.py` <-

- Can you take a **guess** what this code does?
^

- Why make it simple when we can use recursion for a **simple even-odd** check.

- **Bonus points** for embeding the logic within private helper functions to further complicate the understanding.

---

-> `src/7_commenting_out_code.py` <-

- **Never delete** old code, just comment it out.
  
- It's like an **archeological dig** for future coders!
  
- Mix actual code with large commented sections to **obscure** the current functionality.

---

-> `src/8_misleading_comments.py` <-

- Comments should **seldom** match the code's purpose.
  
- **Confuse and conquer**!

---

-> `src/9_redundant_code.py` <-

- **Redundancy** is key.
  
- Let them ponder the **purpose** of your code.

---

-> `src/10_creative_use_of_data_types.py` <-

- Data types? Just a **suggestion**.
  
- Mix and match for maximum **confusion**.

---

-> Protip: Lower Case **l** Looks a Lot Like the Digit **1** <-
^

- Use lower case l to indicate long constants. 
^

- e.g. `10l` is more likely to be mistaken for `101`. Ban any fonts that clearly disambiguate `uvw wW gq9 2z 5s il17|!j oO08 `'" ;,. m nn rn {[()]}`. 
  
- Be creative.

---

-> `src/11_unnecessary_complexity.py` <-

- Wrap **everything** in `try-except`.
  
- ~Even~ Especially, when it's not **needed**.

---


-> `src/12_arbitrary_restrictions.py` <-

- Introduce **random** restrictions.
  
- Make them wonder why `4` is so special.

---


-> `src/13_cryptic_algorithms.py` <-

- The more **cryptic**, the **better**.
  
- Make simple algorithms look **complex**.
  
  ^

```python
def cryptic_algo(a, b):
    return a * b - a / b + a % b
```

---

-> `src/14_repetitive_code.py` <-

- Don't use `elif` or `switch`.
  
- Repetition is your ally.

---

-> `src/15_misuse_of_language.py` <-


- **Mix** languages in your code.
  
- Use variable names from **different languages** for an **international flair**.
  
- Maintenance coders, without your firm grasp of Spanish, will enjoy the **multicultural experience** of deciphering the meaning.

---

-> Protip: Try to pack as much as possible into a **single** line. <- 

This saves the overhead of temporary variables, and makes source files **shorter** by eliminating new line characters and white space. 

> Good programmers can often hit the **255 character** line length limit imposed by some IDEs.

---

-> `src/16_redefine_standard_functions.py` <-

- Redefine len to return **half** the actual length.
  
- Change sum to return the **maximum** value instead of the sum.
  
- Alter **max** to behave like **min**, or return the first element if no key is provided.

^

> Create a **parallel universe** where nothing works as expected!

---

> If God didn't want us to use global variables, he wouldn't have invented them.

Rather than disappoint God, use and set as many global variables as possible. Each function should use and set **at least two** of them, even if there's no reason to do this.

---

-> `src/17_abusing_global_variables.py` <-

- Use and modify global variables recklessly. They should be in every method!
- Watch as everyone tries to untangle the web of dependencies.
  
---

-> `src/18_overuse_design_patterns.py` <-

- Implement **design patterns** where they **aren'**t needed.
> The more complex, the better.

---

-> Protip: **Never** test your code!
^

> Leaving bugs in your programs gives the maintenance programmer who comes along later something interesting to do. 


---

And last but not the least! 

My favourite... 

---

-> `src/19_toilet_tubing.py`

- **Never** under any circumstances allow the code from more than one function or procedure to appear on the screen at once.

- Comments at the top of procedures should use templates that are **at least 15 lines** long and make liberal use of blank lines.

---


-> # Closing Thoughts <-

- Writing **unmaintainable** code is an **art** form.
- Today, you've taken your first steps to mastering this craft.
- Go forth and code (confusingly) and secure your job! 

---

-> # On a more serious note... <-

> In case you didn't get it, this talk was a **parody** based on a very old paper - "How To Write Unmaintainable Code - Ensure a job for life ;-)" by Roedy Green [1997] modified to use Python examples! 

---

-> # Please: <-

- **Don't** write unmaintainable code. Else it will be `PIP` city soon.
^

- **Do** write code that is easy to understand, collaborate and scale.

---

-> # Another thing! <-
^

> All of the code in this presentation was generated by AI using a mix of **GPT-4** and **Github Copilot** (OpenAI's Codex).

^

> The interesting aspect here is that despite this code being **highly unreadable** and **unusable** in a real-world scenario(for Humans), it is still syntactically correct and can be executed and in most cases will produce the expected output at near same performance as the optimised code. `Sharing an instance from...`.

---

> So, if you are a **junior developer** and you are struggling to understand the code written by your **senior developer**, it's not your fault.
^

> But you should use this as an opportunity to learn and improve your skills and don't be shy to supplement your knowledge using AI tools like **Github Copilot** 
^

> Do ensure your **foundation** of knowledge is **solid**, because AI tools can be **highly unreliable** while being **super confident**.

---

> Don't be naive to stick to the **old ways** of doing things, **embrace** the **better** to **improve** your **productivity**.
^

> Don't fall into the trap of being a **Real** programmer. 
 
-> `res/real_programmers.png` <-

---

-> # Thank You! <-

**Any questions?**

---

All the code used in this presentation will be available on **Github**.

I will share the repo link shortly on **Twitter**. 

---


-> █▀▀▀▀▀█  ▄▄▀▀▄█ ▄ █▀▀▀▀▀█  <-
-> █ ███ █ ▄   █▄ █▄ █ ███ █  <-
-> █ ▀▀▀ █ ▀▀ ▄▄█  ▀ █ ▀▀▀ █  <-
-> ▀▀▀▀▀▀▀ ▀ █▄▀ █ █ ▀▀▀▀▀▀▀  <-
-> █▀▄ ▄█▀▀ █ ▀▄▀▀█▀  ▄██▄▄   <-
-> ▀▄███▀▀█▀▄▀ ▄▀ ▀▀▄▀▄██ ▀█  <-
-> █▄▄█▄▀▀ ▀▀ ▀▀▄ ██ ▀▀   ▄▀  <-
-> █  █▀▀▀▀  ▄█▀ ▀█▄█   ▀▄▀█  <-
-> ▀ ▀▀ ▀▀▀█▀█▀█▀▀ █▀▀▀█ █    <-
-> █▀▀▀▀▀█ █▀ █▄▀█▄█ ▀ █▀ ▄█  <-
-> █ ███ █  █ █▀███▀███▀█▀▄▄  <-
-> █ ▀▀▀ █ ▄▀█ ▄ ▀ █▄ █▄ ▀ █  <-
-> ▀▀▀▀▀▀▀ ▀   ▀  ▀▀ ▀  ▀  ▀  <-
