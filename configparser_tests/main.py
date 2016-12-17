import configparser
Config = configparser.ConfigParser()
Config.read('example.ini')


def config_section_map(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

Name = config_section_map("SectionOne")['name']
Age = config_section_map("SectionOne")['age']
print("Hello %s. You are %s years old." % (Name, Age))