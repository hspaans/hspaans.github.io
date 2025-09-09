.. post:: 2025-09-09 10:00:00
    :tags: LinkedIn, Python, performance, fun, benchmarking
    :category: Random

One billion nested loop iterations
==================================

A few days ago I was `reading a post on LinkedIn <https://www.linkedin.com/feed/update/urn:li:activity:7370840117663674370/>`_ about a performance comparison between Python and other language. The author made a benchmark with a nested loop of one billion iterations in both languages and concluded that C and Rust was much faster than Python. As I was curious about this claim, I decided to replicate the benchmark myself and see if I could achieve similar results and how much of this post was true.

.. note::

   **This benchmark is mostly done for fun and educational purposes on GitHub Codespaces.**

As no code was provided in the post, all the code had to be created from scratch. The benchmark consists of a nested loop where the outer loop runs 100,000 times and the inner loop runs 10,000 times, resulting in a total of 1 billion iterations (10^5 * 10^4 = 10^9). A counter variable is incremented in each iteration to ensure that the loops are not optimized away by the compiler or interpreter. And generating the source code for different languages was an ideal task for `Google Gemini <https://gemini.google.com/app>`_ with some hints from `GitHub Copilot <https://github.com/features/copilot>`_.

.. warning::

   The following code snippets are for educational purposes only and may not represent best practices for performance benchmarking or to have the most efficient code in each language.

Python Benchmark
----------------

Here is the Python code I used for the benchmark:

.. code-block:: python
    :caption: Python code for one billion nested loop iterations

    import time

    def nested_loop_counter():
        """
        Performs 1 billion nested loop iterations and measures the execution time.

        The outer loop runs 100,000 times and the inner loop runs 10,000 times,
        resulting in a total of 1,000,000,000 iterations (10^5 * 10^4 = 10^9).
        """
        print("Starting the nested loop counter...")
        start_time = time.time()

        # Initialize a counter variable
        count = 0

        # Outer loop runs 100,000 times
        for i in range(100000):
            # Inner loop runs 10,000 times
            for j in range(10000):
                count += 1

        end_time = time.time()

        # Calculate the total execution time
        elapsed_time = end_time - start_time

        print("\n--- Execution Finished ---")
        print(f"Total iterations: {count}")
        print(f"Time taken: {elapsed_time:.2f} seconds")
        print("------------------------")

    # Run the program
    if __name__ == "__main__":
        nested_loop_counter()

The results of the Python benchmark were as follows:

.. code-block:: console
    :caption: Python benchmark execution output

    $ python3 onebillion.py 
    Starting the nested loop counter...

    --- Execution Finished ---
    Total iterations: 1000000000
    Time taken: 22.81 seconds
    ------------------------

And with 22.81 seconds, Python was indeed not the fastest language for this benchmark. As a comparison, I also ran the code with PyPy, which is an alternative implementation of Python that often provides better performance for long-running tasks. The results with PyPy were significantly better:

.. code-block:: console
    :caption: PyPy benchmark execution output

    $ pypy3 onebillion.py 
    Starting the nested loop counter...

    --- Execution Finished ---
    Total iterations: 1000000000
    Time taken: 0.51 seconds
    ------------------------

Java Benchmark
--------------
Here is the equivalent Java code for the benchmark:

.. code-block:: java
    :caption: Java code for one billion nested loop iterations

    import java.lang.System;

    public class nested_loop_counter {

        public static void main(String[] args) {

            // Use 'long' for the counter and loop variables to ensure they can
            // handle a very large number of iterations without overflowing.
            long count = 0;

            System.out.println("Starting the nested loop counter...");

            // Start the timer using nanoseconds for high precision
            long startTime = System.nanoTime();

            // The outer loop runs 100,000 times
            for (long i = 0; i < 100000; i++) {
                // The inner loop runs 10,000 times
                for (long j = 0; j < 10000; j++) {
                    count++;
                }
            }

            // Stop the timer
            long endTime = System.nanoTime();
            
            // Calculate the elapsed time in seconds
            double elapsedTimeInSeconds = (endTime - startTime) / 1_000_000_000.0;

            System.out.println("\n--- Execution Finished ---");
            System.out.println("Total iterations: " + count);
            System.out.printf("Time taken: %.2f seconds\n", elapsedTimeInSeconds);
            System.out.println("------------------------");
        }
    }

Luckily, modern Java development environments and build tools allow developers to compile their code more easily for development purposes. The results of the Java benchmark were as follows:

.. code-block:: console
    :caption: Output of Java benchmark for one billion nested loop iterations

    $ java onebillion.java
    Starting the nested loop counter...

    --- Execution Finished ---
    Total iterations: 1000000000
    Time taken: 0.23 seconds
    ------------------------

The results show that Java is indeed faster than Python for this benchmark, completing the task in just 0.23 seconds. Overall quite impressive to see how much the JVM has improved over the years.

Golang Benchmark
----------------

Here is the equivalent Go code for the benchmark:

.. code-block:: go
    :caption: Go code for one billion nested loop iterations

    package main

    import (
            "fmt"
            "time"
    )

    func main() {
            // Use int64 for the counter to handle the large number of iterations.
            var count int64 = 0

            fmt.Println("Starting the nested loop counter...")

            // Start the timer
            start := time.Now()

            // The outer loop runs 100,000 times
            for i := 0; i < 100000; i++ {
                    // The inner loop runs 10,000 times
                    for j := 0; j < 10000; j++ {
                            count++
                    }
            }

            // Stop the timer
            elapsed := time.Since(start)

            fmt.Println("\n--- Execution Finished ---")
            fmt.Printf("Total iterations: %d\n", count)
            fmt.Printf("Time taken: %s\n", elapsed)
            fmt.Println("------------------------")
    }

Like Java, Go also has a built-in compiler as part of the Go toolchain. The results of the Go benchmark were as follows:

.. code-block:: console
    :caption: Output of Go benchmark for one billion nested loop iterations

    $ go run onebillion.go
    Starting the nested loop counter...

    --- Execution Finished ---
    Total iterations: 1000000000
    Time taken: 130.028666ms
    ------------------------

The results show that Go is also quite fast for this benchmark, completing the task in just 130 milliseconds. This performance is comparable to Java, demonstrating Go's efficiency in handling such tasks.

Perl Benchmark
--------------

Here is the equivalent Perl code for the benchmark:

.. code-block:: perl
    :caption: Perl code for one billion nested loop iterations

    use strict;
    use warnings;
    use Time::HiRes qw(time);

    # Use a scalar variable for the counter. Perl handles large numbers automatically.
    my $count = 0;

    print "Starting the nested loop counter...\n";

    # Start the timer
    my $start_time = time();

    # Outer loop runs 100,000 times
    for (my $i = 0; $i < 100000; $i++) {
        # Inner loop runs 10,000 times
        for (my $j = 0; $j < 10000; $j++) {
            $count++;
        }
    }

    # Stop the timer
    my $end_time = time();

    # Calculate the total execution time
    my $elapsed_time = $end_time - $start_time;

    print "\n--- Execution Finished ---\n";
    print "Total iterations: $count\n";
    printf "Time taken: %.2f seconds\n", $elapsed_time;
    print "------------------------\n";

For Perl, the interpreter is usually included in the standard installation, but the HiRes module is required for high-resolution timing and needs to be installed separately. The results of the Perl benchmark were as follows:

.. code-block:: console
    :caption: Output of Perl benchmark for one billion nested loop iterations

    $ perl onebillion.pl
    Starting the nested loop counter...

    --- Execution Finished ---
    Total iterations: 1000000000
    Time taken: 15.24 seconds
    ------------------------

The results show that Perl is indeed faster than Python for this benchmark, completing the task in just 15.24 seconds. While this is faster than Python, it is still slower than both Java and Go.

Clang Benchmark
---------------

Here is the equivalent C code for the benchmark:

.. code-block:: c
    :caption: C code for one billion nested loop iterations

    #include <stdio.h>
    #include <time.h>

    int main() {
        // Use long long for the counter to avoid integer overflow, as 1 billion
        // exceeds the maximum value of a standard int on many systems.
        long long count = 0;

        printf("Starting the nested loop counter...\n");

        // Start the timer
        clock_t start_time = clock();

        // Outer loop runs 100,000 times
        for (long long i = 0; i < 100000; i++) {
            // Inner loop runs 10,000 times
            for (long long j = 0; j < 10000; j++) {
                count++;
            }
        }

        // Stop the timer
        clock_t end_time = clock();

        // Calculate the total execution time in seconds
        double elapsed_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;

        printf("\n--- Execution Finished ---\n");
        printf("Total iterations: %lld\n", count);
        printf("Time taken: %.2f seconds\n", elapsed_time);
        printf("------------------------\n");

        return 0;
    }

For C, the GCC compiler is commonly used and is part of the GNU Compiler Collection. The results of the C benchmark were as follows without any optimizations:

.. code-block:: console
    :caption: Output of C benchmark compiled without optimizations

    $ gcc onebillion.c 
    $ ./a.out 
    Starting the nested loop counter...

    --- Execution Finished ---
    Total iterations: 1000000000
    Time taken: 0.40 seconds
    ------------------------

But with optimizations enabled using the `-O2` or `-O3` flag, the performance improved significantly:

.. code-block:: console
    :caption: C benchmark output with GCC -O3 optimizations enabled

    $ gcc -O3 onebillion.c
    $ ./a.out
    Starting the nested loop counter...

    --- Execution Finished ---
    Total iterations: 1000000000
    Time taken: 0.00 seconds
    ------------------------

Maybe a bit too fast to be true, but the compiler optimizations really make a big difference in performance for this benchmark. And secondly the resolution of the timer is not high enough to measure the time accurately. So the actual time is likely a few milliseconds, but it is reported as 0.00 seconds due to rounding.

Rust Benchmark
--------------

Here is the equivalent Rust code for the benchmark:

.. code-block:: rust
    :caption: Rust code for one billion nested loop iterations

    use std::time::Instant;

    fn main() {
        // Use u64 for the counter and loop variables to ensure they can handle
        // a very large number of iterations without overflow.
        let mut count: u64 = 0;

        println!("Starting the nested loop counter...");

        // Start the timer
        let start_time = Instant::now();

        // Outer loop runs 100,000 times
        for i in 0..100000 {
            // Inner loop runs 10,000 times
            for j in 0..10000 {
                count += 1;
            }
        }

        // Stop the timer and calculate the duration
        let end_time = Instant::now();
        let elapsed_time = end_time.duration_since(start_time);

        println!("\n--- Execution Finished ---");
        println!("Total iterations: {}", count);
        println!("Time taken: {:.2?} seconds", elapsed_time);
        println!("------------------------");
    }

Lets see how Rust performs in this benchmark. The results of the Rust benchmark were as follows without any optimizations:

.. code-block:: console
    :caption: Output of Rust benchmark (no optimizations)

    $ rustc onebillion.rs
    warning: unused variable: `i`
    --> onebillion.rs:14:9
    |
    14 |     for i in 0..100000 {
    |         ^ help: if this is intentional, prefix it with an underscore: `_i`
    |
    = note: `#[warn(unused_variables)]` on by default

    warning: unused variable: `j`
    --> onebillion.rs:16:13
    |
    16 |         for j in 0..10000 {
    |             ^ help: if this is intentional, prefix it with an underscore: `_j`

    warning: 2 warnings emitted

    $ ./onebillion 
    Starting the nested loop counter...

    --- Execution Finished ---
    Total iterations: 1000000000
    Time taken: 2.24s seconds
    ------------------------

If we ignore the warnings about unused variables, Rust performs quite well, completing the task in just 2.24 seconds. However, with optimizations enabled using the `-O` flag, the performance improved significantly:

.. code-block:: console
    :caption: Rust benchmark output with optimizations (-O flag)

    $ rustc -O onebillion.rs
    warning: unused variable: `i`
    --> onebillion.rs:14:9
    |
    14 |     for i in 0..100000 {
    |         ^ help: if this is intentional, prefix it with an underscore: `_i`
    |
    = note: `#[warn(unused_variables)]` on by default

    warning: unused variable: `j`
    --> onebillion.rs:16:13
    |
    16 |         for j in 0..10000 {
    |             ^ help: if this is intentional, prefix it with an underscore: `_j`

    warning: 2 warnings emitted

    $ ./onebillion 
    Starting the nested loop counter...

    --- Execution Finished ---
    Total iterations: 1000000000
    Time taken: 154.00ns seconds
    ------------------------

And the results show that with optimizations, Rust can complete the task in just 154 nanoseconds. This performance is comparable to C with optimizations, demonstrating Rust's efficiency in handling such tasks.

But lets fix the warnings by prefixing the unused variables with an underscore as Gemini wasn't aware of this:

.. code-block:: console
    :caption: Rust benchmark output with optimizations and fixed warnings

    $ rustc -O onebillion.rs
    $ ./onebillion 
    Starting the nested loop counter...

    --- Execution Finished ---
    Total iterations: 1000000000
    Time taken: 66.00ns seconds
    ------------------------

This time the performance improved even further, completing the task in just 66 nanoseconds. This shows that addressing compiler warnings can lead to better optimizations and improved performance.

Conclusion about performance
----------------------------

After running the benchmarks in different languages, the results were as followed: Don't take these numbers too seriously as they can vary based on the system, compiler/interpreter versions, and other factors. But they do give a general idea of the performance differences between the languages for this specific task. And don't believe everything you `read on LinkedIn <https://www.linkedin.com/feed/update/urn:li:activity:7370840117663674370/>`_.

Raw processing performance is only one aspect of a programming language. Other factors like developer productivity, ecosystem, libraries, community support, and specific use cases also play a significant role in choosing the right language for a project. But marking a language as slow or fast based on one benchmark is not a good idea as it doesn't take into account the full context of software development.
