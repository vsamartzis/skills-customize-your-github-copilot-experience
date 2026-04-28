#!/usr/bin/env python3
"""Generate README files for all 100 assignments and update config.json"""

import json
import os
from datetime import datetime, timedelta

# Define all 100 assignments with detailed information
assignments = [
    # Fundamentals (10)
    ("variables-and-types", "Variables and Data Types", "Learn about primitive data types and variable assignment in Python"),
    ("operators", "Basic Operators", "Master arithmetic, logical, and comparison operators"),
    ("conditionals", "Conditional Statements", "Use if-else statements for decision making"),
    ("loops-basics", "Loop Fundamentals", "Implement for and while loops for repetition"),
    ("functions-intro", "Introduction to Functions", "Define and call reusable functions"),
    ("strings", "String Manipulation", "Work with string methods and formatting"),
    ("lists", "Lists and Arrays", "Use Python lists to store and manipulate data"),
    ("input-output", "Input and Output", "Create programs that interact with users"),
    ("type-conversion", "Type Conversion", "Convert between different data types"),
    ("comments-documentation", "Comments and Documentation", "Write clear code with proper documentation"),
    
    # Data Structures (10)
    ("dictionaries", "Dictionaries and Maps", "Use key-value pairs for data organization"),
    ("tuples", "Tuples and Immutability", "Work with immutable sequences"),
    ("sets", "Sets and Unique Values", "Use sets for storing unique elements"),
    ("nested-structures", "Nested Data Structures", "Work with complex nested lists and dictionaries"),
    ("stack-implementation", "Stack Data Structure", "Implement a stack with push and pop operations"),
    ("queue-implementation", "Queue Data Structure", "Implement a queue with enqueue and dequeue"),
    ("linked-list", "Linked Lists", "Create a singly linked list from scratch"),
    ("binary-tree", "Binary Trees", "Build and traverse binary tree structures"),
    ("graph-basics", "Graph Fundamentals", "Create and traverse graph data structures"),
    ("hash-tables", "Hash Tables and Hashing", "Understand hash functions and collision handling"),
    
    # Algorithms (10)
    ("bubble-sort", "Bubble Sort Algorithm", "Implement and understand bubble sorting"),
    ("quick-sort", "Quick Sort Algorithm", "Master the quick sort algorithm"),
    ("merge-sort", "Merge Sort Algorithm", "Implement divide-and-conquer sorting"),
    ("binary-search", "Binary Search", "Use binary search on sorted arrays"),
    ("linear-search", "Linear Search", "Implement sequential search algorithms"),
    ("fibonacci-sequence", "Fibonacci Numbers", "Generate Fibonacci sequence recursively and iteratively"),
    ("prime-numbers", "Prime Number Checker", "Identify and generate prime numbers"),
    ("gcd-lcm", "GCD and LCM", "Calculate greatest common divisor and least common multiple"),
    ("pattern-matching", "Pattern Matching", "Search for patterns in strings"),
    ("recursion-advanced", "Advanced Recursion", "Solve problems using recursive algorithms"),
    
    # Object-Oriented Programming (10)
    ("classes-objects", "Classes and Objects", "Design and implement classes"),
    ("inheritance", "Inheritance in OOP", "Create class hierarchies with inheritance"),
    ("polymorphism", "Polymorphism", "Implement method overriding and dynamic dispatch"),
    ("encapsulation", "Encapsulation", "Use access modifiers and information hiding"),
    ("abstraction", "Abstraction", "Design abstract base classes and interfaces"),
    ("static-members", "Static Methods and Variables", "Work with class-level members"),
    ("constructors", "Constructors and Initialization", "Implement object initialization"),
    ("composition", "Composition vs Inheritance", "Choose composition over inheritance wisely"),
    ("properties", "Properties and Getters/Setters", "Use properties for controlled access"),
    ("design-patterns-basic", "Singleton Pattern", "Implement the Singleton design pattern"),
    
    # Web Development (10)
    ("html-basics", "HTML Fundamentals", "Create structured HTML documents"),
    ("css-styling", "CSS Styling Basics", "Apply styles to HTML elements"),
    ("javascript-basics", "JavaScript Fundamentals", "Write interactive JavaScript code"),
    ("dom-manipulation", "DOM Manipulation", "Modify HTML elements with JavaScript"),
    ("event-handling", "Event Handling", "Respond to user interactions"),
    ("forms-validation", "Form Validation", "Validate user input in web forms"),
    ("flexbox-layout", "Flexbox Layout", "Create flexible responsive layouts"),
    ("css-grid", "CSS Grid Layout", "Build complex layouts with CSS Grid"),
    ("responsive-design", "Responsive Web Design", "Make websites work on all devices"),
    ("fetch-api", "Fetch API and AJAX", "Load data asynchronously from servers"),
    
    # Databases & SQL (10)
    ("sql-basics", "SQL Fundamentals", "Write basic SQL queries"),
    ("create-tables", "Creating Tables", "Design and create database tables"),
    ("select-queries", "SELECT Queries", "Retrieve data with various SQL queries"),
    ("where-clause", "WHERE and Filtering", "Filter data with WHERE conditions"),
    ("joins", "SQL JOINS", "Combine data from multiple tables"),
    ("group-by", "GROUP BY and Aggregation", "Summarize data with aggregate functions"),
    ("subqueries", "Subqueries", "Use nested queries for complex logic"),
    ("indexes", "Database Indexing", "Optimize queries with indexes"),
    ("transactions", "Database Transactions", "Implement ACID transactions"),
    ("normalization", "Database Normalization", "Design normalized database schemas"),
    
    # File I/O & System Programming (10)
    ("file-reading", "Reading Files", "Open and read file contents"),
    ("file-writing", "Writing Files", "Create and write to files"),
    ("text-processing", "Text File Processing", "Parse and analyze text files"),
    ("csv-handling", "CSV File Handling", "Read and write CSV files"),
    ("json-parsing", "JSON Parsing", "Work with JSON data"),
    ("directory-operations", "Directory Operations", "List, create, and delete directories"),
    ("path-manipulation", "Path Manipulation", "Work with file and directory paths"),
    ("regular-expressions", "Regular Expressions", "Use regex for pattern matching"),
    ("command-line-args", "Command Line Arguments", "Process command line input"),
    ("environment-variables", "Environment Variables", "Read and use environment variables"),
    
    # Testing and Quality (8)
    ("unit-testing", "Unit Testing Basics", "Write unit tests with frameworks"),
    ("test-coverage", "Test Coverage", "Measure and improve code coverage"),
    ("mocking", "Mocking and Stubs", "Mock dependencies in tests"),
    ("integration-testing", "Integration Testing", "Test multiple components together"),
    ("assertions", "Test Assertions", "Use assertions to verify behavior"),
    ("debugging-techniques", "Debugging Techniques", "Use debuggers and logging effectively"),
    ("code-quality", "Code Quality Metrics", "Measure and improve code quality"),
    ("refactoring", "Refactoring Code", "Improve code structure and readability"),
    
    # APIs and Networking (8)
    ("rest-apis", "REST API Basics", "Understand REST principles"),
    ("http-methods", "HTTP Methods", "Use GET, POST, PUT, DELETE correctly"),
    ("json-apis", "JSON APIs", "Work with JSON-based APIs"),
    ("api-authentication", "API Authentication", "Implement API key and token auth"),
    ("error-handling-api", "API Error Handling", "Handle HTTP errors properly"),
    ("webhooks", "Webhooks", "Receive and process webhook events"),
    ("rate-limiting", "Rate Limiting", "Implement and handle rate limits"),
    ("socket-programming", "Socket Programming", "Use sockets for network communication"),
    
    # Functional Programming (8)
    ("map-filter", "Map and Filter", "Use functional programming techniques"),
    ("lambda-functions", "Lambda Functions", "Create anonymous functions"),
    ("list-comprehensions", "List Comprehensions", "Use elegant list creation syntax"),
    ("higher-order-functions", "Higher-Order Functions", "Functions that take function arguments"),
    ("closures", "Closures", "Understand variable scope and closures"),
    ("decorators", "Decorators", "Implement function decorators"),
    ("generators", "Generator Functions", "Create lazy iterators"),
    ("immutable-data", "Immutable Data Structures", "Work with immutable collections"),
    
    # Performance and Optimization (8)
    ("big-o-notation", "Big O Notation", "Analyze algorithm complexity"),
    ("algorithm-complexity", "Algorithm Complexity Analysis", "Measure time and space complexity"),
    ("caching-strategies", "Caching Strategies", "Implement caching for performance"),
    ("memoization", "Memoization", "Cache function results"),
    ("code-profiling", "Code Profiling", "Identify performance bottlenecks"),
    ("memory-management", "Memory Management", "Optimize memory usage"),
    ("lazy-evaluation", "Lazy Evaluation", "Defer computation until needed"),
    ("parallel-processing", "Parallel Processing", "Use threading and multiprocessing"),
    
    # Games and Graphics (10)
    ("pygame-basics", "Pygame Fundamentals", "Create 2D games with Pygame"),
    ("sprite-management", "Sprite Management", "Handle game objects and sprites"),
    ("collision-detection", "Collision Detection", "Detect object collisions"),
    ("game-loop", "Game Loop Implementation", "Implement the game loop"),
    ("animation", "Animation and Movement", "Animate sprites and objects"),
    ("sound-effects", "Sound and Music", "Add audio to games"),
    ("user-input", "User Input Handling", "Respond to keyboard and mouse input"),
    ("game-state", "Game State Management", "Manage different game states"),
    
    # Data Analysis (8)
    ("loading-data", "Loading Data", "Import data from various sources"),
    ("pandas-dataframes", "Pandas DataFrames", "Work with pandas data structures"),
    ("data-filtering", "Data Filtering", "Select specific rows and columns"),
    ("aggregation", "Data Aggregation", "Summarize data with aggregations"),
    ("visualization", "Data Visualization", "Create charts and graphs"),
    ("statistical-analysis", "Statistical Analysis", "Calculate statistics and distributions"),
    ("grouping-data", "Grouping Data", "Group and aggregate by categories"),
    ("merging-datasets", "Merging Datasets", "Combine multiple datasets"),
    
    # Security (8)
    ("input-validation", "Input Validation", "Validate user input safely"),
    ("sql-injection", "SQL Injection Prevention", "Prevent SQL injection attacks"),
    ("xss-prevention", "XSS Prevention", "Prevent cross-site scripting"),
    ("password-hashing", "Password Hashing", "Hash and verify passwords"),
    ("encryption-basics", "Encryption Basics", "Implement basic encryption"),
    ("authentication", "Authentication Systems", "Build login and authentication"),
    ("access-control", "Access Control", "Implement authorization and roles"),
    ("secure-coding", "Secure Coding Practices", "Write security-focused code"),
    
    # Projects (4)
    ("project-tic-tac-toe", "Project: Tic-Tac-Toe Game", "Build a complete tic-tac-toe game"),
    ("project-todo-app", "Project: Todo Application", "Create a full task management app"),
]

# Ensure we have exactly 100 assignments
assert len(assignments) == 100, f"Expected 100 assignments, got {len(assignments)}"

def generate_readme(title, description):
    """Generate README content for an assignment"""
    template = f"""# 📘 Assignment: {title}

## 🎯 Objective

{description}

## 📝 Tasks

### 🛠️ Task 1: Core Implementation

#### Description
Implement the main functionality for this assignment. Write clean, well-organized code that demonstrates your understanding of the core concepts.

#### Requirements
Completed program should:

- Demonstrate all key concepts related to {title.lower()}
- Include clear variable names and comments
- Handle edge cases appropriately
- Follow Python best practices

### 🛠️ Task 2: Testing and Validation

#### Description
Test your implementation with multiple test cases to ensure it works correctly.

#### Requirements
Completed program should:

- Include test cases for normal scenarios
- Handle error cases gracefully
- Display output clearly for verification
- Include comments explaining test cases

### 🛠️ Task 3: Documentation and Reflection

#### Description
Document your code and write a brief reflection on what you learned.

#### Requirements
Completed program should:

- Include docstrings for all functions
- Provide clear comments explaining complex logic
- Include a brief summary of key learnings
- Suggest possible extensions or improvements
"""
    return template

def generate_config_json(assignments):
    """Generate the config.json file with all assignments"""
    base_date = datetime(2025, 1, 1)
    
    config = {
        "course": {
            "title": "Computer Science",
            "school": "Mergington High School",
            "description": "Introduction to programming and computer science"
        },
        "assignments": []
    }
    
    for idx, (folder_name, title, description) in enumerate(assignments):
        due_date = base_date + timedelta(days=idx * 2)
        due_date_str = due_date.strftime("%Y-%m-%d")
        
        assignment = {
            "id": folder_name,
            "title": title,
            "description": description,
            "path": f"assignments/{folder_name}",
            "dueDate": due_date_str
        }
        config["assignments"].append(assignment)
    
    return config

def main():
    """Create all README files and update config.json"""
    base_path = "/workspaces/skills-customize-your-github-copilot-experience"
    
    # Generate README files
    for idx, (folder_name, title, description) in enumerate(assignments):
        folder_path = os.path.join(base_path, "assignments", folder_name)
        readme_path = os.path.join(folder_path, "README.md")
        
        if not os.path.exists(readme_path):
            content = generate_readme(title, description)
            with open(readme_path, 'w') as f:
                f.write(content)
            print(f"✓ Created README for {folder_name}")
        else:
            print(f"⊘ README already exists for {folder_name}")
    
    # Generate config.json
    config = generate_config_json(assignments)
    config_path = os.path.join(base_path, "config.json")
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"\n✓ Updated config.json with {len(assignments)} assignments")
    print(f"✓ All assignments have past due dates (historical assignments)")

if __name__ == "__main__":
    main()
