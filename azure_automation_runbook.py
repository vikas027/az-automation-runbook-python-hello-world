#!/usr/bin/env python
"""
Azure Automation Runbook - Hello World Example

This script demonstrates how to import and use the hello-world package
in a simple automation runbook scenario.
"""

import sys
import hello_world


def main():
    """
    Main function that demonstrates using the hello-world package.
    """
    print("🚀 Starting Azure Automation Runbook...")
    print("=" * 50)

    try:
        # Method 1: Direct call to the main function
        print("📦 Calling hello_world.main() directly:")
        hello_world.main()
        print()

        # Method 2: Check if the function exists and get its details
        print("🔍 Inspecting the hello_world package:")
        if hasattr(hello_world, 'main'):
            print("✅ hello_world.main() function found")
            print(f"📋 Function documentation: {hello_world.main.__doc__ or 'No documentation'}")
        else:
            print("❌ hello_world.main() function not found")
        print()

        # Method 3: Custom integration example
        print("🔧 Custom automation logic:")
        print("This demonstrates how you can integrate the hello-world package")
        print("into your automation workflows...")

        # Simulate some automation steps
        steps = [
            "Initializing automation environment",
            "Loading configuration",
            "Executing hello-world package",
            "Processing results",
            "Cleanup and finalization"
        ]

        for i, step in enumerate(steps, 1):
            print(f"  {i}. {step}")
            if "hello-world" in step:
                print("    ↳ ", end="")
                hello_world.main()

        print()
        print("✅ Automation runbook completed successfully!")

    except Exception as e:
        print(f"❌ Error occurred: {e}")
        return 1

    return 0


if __name__ == "__main__":
    # Exit with the return code from main()
    sys.exit(main())
