"""This is the main script for the runner, it will be used to various methods."""

from sys import platform
from argparse import ArgumentParser
from dotenv import load_dotenv

from os import (
    path,
    getcwd,
    chdir,
    mkdir,
    remove,
    rename
)

from subprocess import (
    Popen,
    check_output
)

from utilities import Utilities as util

class Runner:
    """The runner class which will be used to run, compile and update the server."""

    def __init__(self) -> None:
        pass

    def compile(self, filename: str) -> None:
        """
        This method will be used to compile the server

        Args:
            filename (str): The filename of the server

        Returns:
            str: The output of the compiler
        """
        util.message("blue", f"Compiling the server with filename: {filename}", "🔨")
        if not path.exists(filename):
            util.message("red", "The server file does not exists", "❌")
        if not filename.endswith(util.PAWN_EXT):
            util.message("red", "The server file does not have the .pwn extension", "❌")
        try:
            output = check_output([path.join(getcwd(), util.PAWNO_PATH), filename])
            util.message("green", "The server has been compiled successfully", "✅")
            return util.throw_log(
                "Compilation is going all okay", { 
                    str(output)
                }
            )
        except Exception as error:
            util.message("red", f"The server could not be compiled: {error}", "❌")

    def run_server() -> None:
        """
        This method will be used to run the server

        Args:
            This method has no arguments
        
        Returns:
            None
        """
        util.message("blue", "Running the server", "🚀")
        if platform == "win32":
            server_exe = "samp-server.exe" if platform == "win32" else "samp03svr"
        chdir(path.join(getcwd(), "server"))
        return Popen(["start", "cmd", "/c", server_exe], shell=True)

    def update(filename: str) -> None:
        """
        This method will be used to update the server

        Args:
            filename (str): The filename of the server

        Returns:
            None        
        """
        util.message("blue", "Updating the server", "🔄")
        if not path.exists(filename):
            util.message("red", "The server file does not exists", "❌")

        if not filename.endswith(util.PAWNC_EXT):
            util.message("red", "The server file does not have the .amx extension", "❌")
        
        # It'll be depending on the server folder that you allocate "gamemodes" directory -> default: server/gamemodes
        server_folder = path.join(getcwd(), "server", "gamemodes")

        if not path.exists(server_folder):
            util.message("red", "The server folder does not exists", "❌")
            mkdir(server_folder)
            util.message("green", "The server folder has been created successfully", "✅")
        util.message("blue", f"Moving {filename} to the server folder", "📂")

        if path.exists(path.join(server_folder, filename)):
            remove(path.join(server_folder, filename))

        rename(filename, path.join(server_folder, filename))
        server_cfg = path.join(getcwd(), util.SERVER_CFG_PATH)
        util.message("blue", f"Updating the server.cfg file with {filename}", "📝")

        with open(server_cfg, "r") as file:
            lines = file.readlines()
        with open(server_cfg, "w") as file:
            for line in lines:
                if line.startswith("gamemode"):
                    line = f"gamemode0 {filename.replace('.amx', '')}\n"
                file.write(line)
        return util.message("green", "The server has been updated successfully", "✅")