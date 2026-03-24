from Core.UptimeTracker import uptimeTracker

if __name__ == "__main__":
    uptime = uptimeTracker().get_uptime()
    print(f"System Uptime: {uptime}")