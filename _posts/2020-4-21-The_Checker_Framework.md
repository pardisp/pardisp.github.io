---
layout: post
title: The Checker Framework
tags: software-security software-engineering
---

If you are interested in preventing bugs in your Java project, look no further. The Checker Framework improves Java’s type system through annotations to detect and prevent errors in Java programs. It includes compiler checkers that find bugs or verify the absence of them. The Checker Framework is widely used at Google, Amazon, and Uber.

The built-in type checker in Java, does provide some reasonable type checking and error prevention. However, the Checker Framework lets you define new type checkers and extend the type system and run them as a part of the javac compiler. The checker framework allows the developers to use the available type systems in the framework, or design their own. In this article, we will learn about the most popular checkers in this framework.

## Nullness Checker
The most popular checker in the Checker Framework is the [Nullness Checker](https://checkerframework.org/manual/#nullness-checker). If this checker does not issue any warnings at compile time, it is guaranteed that the program will never throw a null pointer exception. The Nullness Checker is a standard part of the build system at Google.

The most important annotations supported by the Nullness Checker are the following:
* [`@Nullable`](https://checkerframework.org/api/org/checkerframework/checker/nullness/qual/Nullable.html): this annotation indicates a type that has `null` value in its possible set of values. For example, the possible set of values for a `Boolean` is `{true, false, null}`.
* [`@NonNull`](https://checkerframework.org/api/org/checkerframework/checker/nullness/qual/NonNull.html): this annotation indicates a type that does not have `null` in its possible set of values. For example, a variable of type `@NonNull Boolean` only has true and false in its possible set of values.

This checker emits warnings in the following cases:
1. When you dereference an expression that is not `@NonNull`.
2. When the value of a `@NonNull` expression evaluates to `null`.
3. When you assign `null` to a `@NonNull` variable.
4. When a field of type `@NonNull` is not initialized in a constructor.

### Example
```java
@Nullable Object object;
@NonNull Object nonNullObject;
…
object.toString(); // warning: possible null dereference
nonNullObject = object; // warning: nonNullObject might become null
if (nonNullObject == null) doSomething; // warning: redundant check
```


## GUI Effect Checker
When checking graphical user interfaces, the most prevalent bug is invalid thread access by a background process. Well-known GUI frameworks, such as Android and Swing, spawn a single main thread which is known as the UI event thread that is responsible for handling all the events and updates. Any other operation, such as expensive computations, is offloaded to background threads which are known as worker threads. The worker thread should send a request to the main thread to perform any access on its behalf. If any of these background threads directly access a UI element, the framework throws an exception and terminates the application.

This is a challenging issue to debug since it is difficult to remember which methods are permitted to be called on which threads. The [GUI Effect Checker](https://checkerframework.org/manual/#guieffect-checker) solves this problem by allowing the programmer to annotate each method to indicate whether it accesses no UI elements, or whether it may access UI elements. The former method is said to have the safe effect and the latter is said to have the UI effect. A method with the safe effect is prohibited from calling a method with the UI effect.

The most important annotations supported by the GUI Effect Checker are the following:
* [`@SafeEffect`](https://checkerframework.org/api/org/checkerframework/checker/guieffect/qual/SafeEffect.html): this annotation indicates that a method is not allowed to access UI elements.
* [`@UIEffect`](https://checkerframework.org/api/org/checkerframework/checker/guieffect/qual/UIEffect.html): this annotation indicates that a method may access UI elements. Note that it is always safe to call a `@SafeEffect` method whenever it is permitted to call a `@UIEffect` method.

This checker complains in the following cases:
1. When a `@UIEffect` method is invoked by a `@SafeEffect` method.
2. When a supertype declares a @SafeEffect method, and its subtype is overridden as `@UIEffect`.
3. When a method implements or overrides a method in two supertypes and they have different GUI Effect annotations.

### Example
```java
@SafeEffect
public void foo(JTextField tf) {
  tf.setText(“first”); // error since setText is a @UIEffect method,
                       // and is called from a @SafeEffect method.
  Display.syncExec(new Runnable {
    @UIEffect
    public void run() {
      tf.setText(“second”);
    }
  });
}
```


## Tainting Checker
The [Tainting Checker](https://checkerframework.org/manual/#tainting-checker) prevents specific kinds of errors that arise from untrusted or tainted values. These untrusted values come from possibly malicious sources such as user input or unvalidated data. Trust-related errors might cause the application to crash, corrupt data, or leak information. If the checker does not issue any warnings for a correctly-tainted program, no tainted values ever flow to a sensitive sink.

A program must sanitize any untrusted value before using it at any sensitive point in the program. In general, there are two ways to sanitize a value: 1. checking if it is valid, or 2. transforming the value to become valid. An example of the former is to check if the value contains no characters that can be interpreted as SQL commands. An example of the latter is to quote all the characters that can be interpreted as SQL commands.

The Tainting Checker is not aware of the internal semantics of the application, so it cannot warn you correctly if you mis-annotate. The mis-annotation happens in two ways: 1. a sensitive sink annotated as `@Tainted` data, or 2. external data annotated as `@Untainted`. However, as long as you correctly annotate the program points, the checker will ensure there is no undesired information flow.

Some example of the [purposes](https://checkerframework.org/manual/#tainting-many-uses) that the Tainting Checker can serve is as follows:
Prevent SQL injection attacks: external input is `@Tainted`, and @Untainted is checked for SQL syntax.
Prevent cross-site scripting attacks: external input is `@Tainted`, and `@Untainted` is checked for JavaScript syntax.
Prevent information leak: secret data is `@Tainted`, and `@Untainted` may be displayed to the user.


### Example
```java
void processRequest() {
  @Tainted String input = getUserInput();
  executeQuery(input); // error: pass tainted string to executeQuery
}

public String validateInput(String userInput) {
  // Do some validation here.
  @Untainted String result = userInput;
  return result;
}
```


The most important annotations supported by the Tainting Checker are the following:
* [`@Untainted`](https://checkerframework.org/api/org/checkerframework/checker/tainting/qual/Untainted.html): this annotation indicates a type that includes only trusted values.
* [`@Tainted`](https://checkerframework.org/api/org/checkerframework/checker/tainting/qual/Tainted.html): this annotation indicates a type that may include untrusted values. It is a supertype of `@Untainted`.


## Checker Framework in Action
Follow the step-by-step instructions to install and use the Checker Framework to find a security error using the Tainting Checker.

**Step 1: Install**
First, install Java JDK and ANT build tools.
```
$ apt-get install openjdk-8-jdk
$ apt-get install ant
```

Then, follow the instructions to install the checker framework:
```
$ wget https://checkerframework.org/checker-framework-3.3.0.zip
$ unzip checker-framework-3.3.0.zip
$ cd checker-framework-3.3.0
$ pwd
```

Copy the value that is printed to the terminal after running pwd. We will need it later!


**Step 2: Download**
Download the source files from the checker framework website, and unzip it. You will see various examples under the `src` directory. We are going to work with the personal blog demo in this section.
```
$ wget https://checkerframework.org/tutorial/sourcefiles.zip
$ unzip sourcefiles
$ cd src/personalblog-demo
```

**Step 3: Run the Checker**
For building the project, and running the checker at the same time, we use ANT build system to make the process easier. Go ahead and take a look at `src/personalblog-demo/build.xml`. On the 4th line of this file, change the value to the value you copied in the first step. So it will look like this:

```yaml
<property name=”checker-framework” value=”/checker-framework-3.3.0”/>
```

On line 18, the location of the Checker jar file is specified. Then, on line 43, the kind of the checker that we want to use is specified. In this example, we are going to use the Tainting Checker:

```yaml
<compilearg value=”org.checkerframework.checker.tainting.TaintingChecker”/>
```

Now, for building this project with ANT, run the following command:
```
$ ant
```

The checker will emit an error complaining about an untainted string on line 162 of `PersonalBlogService.java`:
```
[jsr308.javac]  + "%' order by post.created desc");
[jsr308.javac]    ^
[jsr308.javac]  found   : @Tainted String
[jsr308.javac]  required: @Untainted String

BUILD FAILED
```


Now that we have identified where the problem is, we can fix the issue in PersonalBlogService.java by forcing the client to only pass an `@Untainted` String to the function `getpostsByCategory()`.

**Step 4: Re-run the Checker**
Using ANT, re-build the modified project. You will see another error on line 55 of `ReadAction.java`:

```
[jsr308.javac]  ...getPostsByCategory(reqCategory));
[jsr308.javac]                        ^
[jsr308.javac]  found   : @Tainted String
[jsr308.javac]  required: @Untainted String

BUILD FAILED
```

This time, we are going to correct the tainting error by validating the string. There is already a `validate()` function in the code that, given any string, validates the string and returns an `@Untainted` one. Use this function to validate `reqCategory`.
After fixing the bug, re-build the project. This time, if corrected properly, the checker will not complain and you should expect the following message:

```
BUILD SUCCESSFUL
```

