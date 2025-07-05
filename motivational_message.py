
import time

def always_try():
    print("🟢 Always try your best...")
    time.sleep(1)
    print("🔧 Do what you need to do while you still have the time.")
    time.sleep(1)
    print("🎯 Opportunity comes only once... grab the chance!")
    time.sleep(1)

def handle_failure():
    print("\n⚠️ Uh-oh! You failed...")
    time.sleep(1)
    print("🧹 Throwing all your worries away...")
    time.sleep(1)
    print("💪 Catching yourself...")
    time.sleep(1)
    print("🙏 Remember, every time you fall,")
    print("✨ You know to Whom you should go — always.")
    time.sleep(1)

def main():
    print("🚀 Starting your motivational journey...
")
    time.sleep(1)
    always_try()

    # Simulating a failure for motivational message
    failed = True
    if failed:
        handle_failure()

    print("\n🌟 Keep going, you're doing great!")

if __name__ == "__main__":
    main()
