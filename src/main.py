def main():
    ourNames = ["Bri", "Cecily"]
    decoration = "~~"
    i = 1
    for name in ourNames:
        print(decoration*i + "Hello world, I'm " + name)
        i += 1

if __name__ == '__main__':
    main()
    