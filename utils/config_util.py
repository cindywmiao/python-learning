import configparser

def config_section_map(Config, section):
    config_dict = {}
    options = Config.options(section)
    for option in options:
        try:
            config_dict[option] = Config.get(section, option)
            if config_dict[option] == -1: print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            config_dict[option] = None
    return config_dict
