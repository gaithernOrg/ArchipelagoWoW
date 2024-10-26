if __name__ == '__main__':
    import ModuleUpdate
    ModuleUpdate.update()

    import Utils
    Utils.init_logging("WOWClient", exception_logger="Client")

    from worlds.wow.Client import launch
    launch()
