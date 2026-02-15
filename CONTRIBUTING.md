# Contributing to Voice Assistant

Thank you for your interest in contributing to the Voice Assistant project! We welcome contributions from the community. This document provides guidelines and instructions for contributing.

## 🎯 Ways to Contribute

- **Report Bugs**: Submit issues for bugs you find
- - **Suggest Features**: Propose new features or improvements
  - - **Submit Code**: Create pull requests with bug fixes or new features
    - - **Improve Documentation**: Help us improve and expand documentation
      - - **Test**: Help test the application on different systems
       
        - ## 📋 Code of Conduct
       
        - - Be respectful and inclusive to all contributors
          - - Provide constructive feedback
            - - Focus on the code, not the person
              - - Help create a welcoming environment
               
                - ## 🐛 Reporting Bugs
               
                - ### Before Submitting
                - 1. Check existing issues to avoid duplicates
                  2. 2. Verify the bug on the latest version
                     3. 3. Gather system information (OS, Python version, etc.)
                       
                        4. ### Creating a Bug Report
                        5. Include:
                        6. - Clear, descriptive title
                           - - Detailed description of the issue
                             - - Steps to reproduce
                               - - Expected vs actual behavior
                                 - - System specifications
                                   - - Relevant logs or screenshots
                                     - - Python version and library versions
                                      
                                       - **Issue Template:**
                                       - ```
                                         ## Description
                                         Brief description of the bug

                                         ## Steps to Reproduce
                                         1. Step one
                                         2. Step two
                                         3. Step three

                                         ## Expected Behavior
                                         What should happen

                                         ## Actual Behavior
                                         What actually happens

                                         ## System Information
                                         - OS: [e.g., Windows 10, Ubuntu 20.04]
                                         - Python Version: [e.g., 3.8.5]
                                         - Microphone: [model if known]
                                         - Arduino: [model/board if applicable]

                                         ## Additional Context
                                         Any other relevant information
                                         ```

                                         ## 💡 Suggesting Features

                                         ### Before Submitting
                                         1. Check existing issues and discussions
                                         2. 2. Ensure the feature aligns with project goals
                                            3. 3. Think through the implementation
                                              
                                               4. ### Creating a Feature Request
                                               5. Include:
                                               6. - Clear title describing the feature
                                                  - - Detailed description of the feature
                                                    - - Why you believe it would be valuable
                                                      - - Possible implementation approaches
                                                        - - Examples or use cases
                                                         
                                                          - **Feature Template:**
                                                          - ```
                                                            ## Feature Description
                                                            What is the feature about?

                                                            ## Use Case
                                                            Why would this feature be useful?

                                                            ## Implementation Ideas
                                                            How could this be implemented?

                                                            ## Additional Context
                                                            Screenshots, examples, or references
                                                            ```

                                                            ## 🚀 Submitting Code

                                                            ### 1. Fork and Clone
                                                            ```bash
                                                            # Fork the repository on GitHub
                                                            # Clone your fork
                                                            git clone https://github.com/YOUR-USERNAME/Voice.git
                                                            cd Voice
                                                            ```

                                                            ### 2. Create a Branch
                                                            ```bash
                                                            # Create a feature branch
                                                            git checkout -b feature/your-feature-name
                                                            # or for bug fixes
                                                            git checkout -b fix/bug-name
                                                            ```

                                                            ### 3. Make Changes
                                                            - Keep commits atomic and focused
                                                            - - Write clear, descriptive commit messages
                                                              - - Follow existing code style
                                                                - - Add comments for complex logic
                                                                 
                                                                  - ### 4. Test Your Changes
                                                                  - ```bash
                                                                    # Test the main application
                                                                    python main.py

                                                                    # Run tests if available
                                                                    python test.py

                                                                    # Check for common issues
                                                                    python -m py_compile main.py jarvis.py test.py
                                                                    ```

                                                                    ### 5. Commit and Push
                                                                    ```bash
                                                                    # Stage your changes
                                                                    git add .

                                                                    # Commit with clear message
                                                                    git commit -m "Add feature: brief description"

                                                                    # Push to your fork
                                                                    git push origin feature/your-feature-name
                                                                    ```

                                                                    ### 6. Create Pull Request
                                                                    - Go to GitHub and create a Pull Request
                                                                    - - Provide clear description of changes
                                                                      - - Reference related issues
                                                                        - - Wait for review and feedback
                                                                         
                                                                          - ## 📝 Commit Message Guidelines
                                                                         
                                                                          - Format:
                                                                          - ```
                                                                            <type>: <subject>

                                                                            <body>

                                                                            <footer>
                                                                            ```

                                                                            Types:
                                                                            - `feat`: New feature
                                                                            - - `fix`: Bug fix
                                                                              - - `docs`: Documentation
                                                                                - - `style`: Code style changes
                                                                                  - - `refactor`: Code refactoring
                                                                                    - - `test`: Test additions/changes
                                                                                      - - `chore`: Build, dependencies, etc.
                                                                                       
                                                                                        - Examples:
                                                                                        - ```
                                                                                          feat: Add voice command logging

                                                                                          fix: Resolve microphone timeout issue

                                                                                          docs: Update installation instructions
                                                                                          ```

                                                                                          ## 🎨 Code Style Guidelines

                                                                                          ### Python Code Style
                                                                                          - Follow PEP 8 conventions
                                                                                          - - Use 4 spaces for indentation
                                                                                            - - Limit lines to 88 characters
                                                                                              - - Use descriptive variable names
                                                                                               
                                                                                                - ### Comments
                                                                                                - - Write clear, concise comments
                                                                                                  - - Explain the "why", not the "what"
                                                                                                    - - Keep comments up-to-date
                                                                                                     
                                                                                                      - ### Function Documentation
                                                                                                      - ```python
                                                                                                        def function_name(param1, param2):
                                                                                                            """
                                                                                                            Brief description of function.

                                                                                                            Args:
                                                                                                                param1: Description of parameter 1
                                                                                                                param2: Description of parameter 2

                                                                                                            Returns:
                                                                                                                Description of return value

                                                                                                            Raises:
                                                                                                                ExceptionType: Description of when raised
                                                                                                            """
                                                                                                        ```
                                                                                                        
                                                                                                        ## 🧪 Testing Guidelines
                                                                                                        
                                                                                                        ### What to Test
                                                                                                        - New features work as expected
                                                                                                        - - Existing functionality isn't broken
                                                                                                          - - Edge cases are handled
                                                                                                            - - Error cases are managed
                                                                                                             
                                                                                                              - ### Testing Commands
                                                                                                              - ```bash
                                                                                                                # Test main application
                                                                                                                python main.py

                                                                                                                # Test specific module
                                                                                                                python -m pytest test.py

                                                                                                                # Test audio functionality
                                                                                                                python test.py --audio

                                                                                                                # Test Arduino communication (if available)
                                                                                                                python test.py --arduino
                                                                                                                ```
                                                                                                                
                                                                                                                ## 📚 Documentation
                                                                                                                
                                                                                                                ### When Adding Features
                                                                                                                - Update README.md if behavior changes
                                                                                                                - - Add comments in the code
                                                                                                                  - - Update configuration section if needed
                                                                                                                    - - Add troubleshooting section if applicable
                                                                                                                     
                                                                                                                      - ### File Documentation
                                                                                                                      - - Update file descriptions in README.md
                                                                                                                        - - Add docstrings to functions
                                                                                                                          - - Include usage examples
                                                                                                                           
                                                                                                                            - ## 🔄 Review Process
                                                                                                                           
                                                                                                                            - 1. **Automated Checks**: Tests and linting run automatically
                                                                                                                              2. 2. **Code Review**: Maintainers review the code
                                                                                                                                 3. 3. **Feedback**: We may request changes
                                                                                                                                    4. 4. **Approval**: Once approved, code is merged
                                                                                                                                      
                                                                                                                                       5. ### What We Look For
                                                                                                                                       6. - Code quality and consistency
                                                                                                                                          - - Test coverage
                                                                                                                                            - - Documentation
                                                                                                                                              - - Backward compatibility
                                                                                                                                                - - Performance impact
                                                                                                                                                 
                                                                                                                                                  - ## 💬 Getting Help
                                                                                                                                                 
                                                                                                                                                  - - Check existing documentation
                                                                                                                                                    - - Search closed issues
                                                                                                                                                      - - Ask in discussions/issues
                                                                                                                                                        - - Review code comments and docstrings
                                                                                                                                                         
                                                                                                                                                          - ## 📦 Development Setup
                                                                                                                                                         
                                                                                                                                                          - ### Requirements
                                                                                                                                                          - - Python 3.6+
                                                                                                                                                            - - Virtual environment (recommended)
                                                                                                                                                              - - Git
                                                                                                                                                               
                                                                                                                                                                - ### Setup Steps
                                                                                                                                                                - ```bash
                                                                                                                                                                  # Clone repository
                                                                                                                                                                  git clone https://github.com/FakhriadiRasyaad/Voice.git
                                                                                                                                                                  cd Voice

                                                                                                                                                                  # Create virtual environment
                                                                                                                                                                  python -m venv venv
                                                                                                                                                                  source venv/bin/activate  # or venv\Scripts\activate on Windows

                                                                                                                                                                  # Install dependencies
                                                                                                                                                                  pip install -r requirements.txt

                                                                                                                                                                  # Install development tools (optional)
                                                                                                                                                                  pip install pytest pylint black
                                                                                                                                                                  ```
                                                                                                                                                                  
                                                                                                                                                                  ### Running Locally
                                                                                                                                                                  ```bash
                                                                                                                                                                  # Activate virtual environment
                                                                                                                                                                  source venv/bin/activate

                                                                                                                                                                  # Run the application
                                                                                                                                                                  python main.py

                                                                                                                                                                  # Run tests
                                                                                                                                                                  python test.py
                                                                                                                                                                  ```
                                                                                                                                                                  
                                                                                                                                                                  ## 🎓 Additional Resources
                                                                                                                                                                  
                                                                                                                                                                  - [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
                                                                                                                                                                  - - [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
                                                                                                                                                                    - - [Python Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
                                                                                                                                                                     
                                                                                                                                                                      - ## 📝 License
                                                                                                                                                                     
                                                                                                                                                                      - By contributing, you agree that your contributions will be licensed under the same license as the project.
                                                                                                                                                                     
                                                                                                                                                                      - ## ✨ Recognition
                                                                                                                                                                     
                                                                                                                                                                      - Contributors will be recognized in the project documentation and commits. Thank you for helping make Voice Assistant better!
                                                                                                                                                                     
                                                                                                                                                                      - ---
                                                                                                                                                                      
                                                                                                                                                                      **Last Updated**: February 15, 2026
                                                                                                                                                                      **Questions?** Open an issue or start a discussion!
                                                                                                                                                                      
