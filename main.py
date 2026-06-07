from rich.console import Console
import os
import json

with open("tools.json") as f:
    data = json.load(f)

console = Console(width=100)

while True:

    os.system("clear")

    console.print("""

████████╗ ██████╗  ██████╗ ██╗     
╚══██╔══╝██╔═══██╗██╔═══██╗██║     
   ██║   ██║   ██║██║   ██║██║     
   ██║   ██║   ██║██║   ██║██║     
   ██║   ╚██████╔╝╚██████╔╝███████╗
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝

""", style="bold bright_green")

    console.print("[bold cyan][1][/bold cyan] Tool List")
    console.print("[bold cyan][2][/bold cyan] Update System")
    console.print("[bold cyan][3][/bold cyan] Exit")

    choice = input("\nWhat is your choice: ")

    if choice == "1":

        os.system("clear")

        console.print("""

████████╗ ██████╗  ██████╗ ██╗     
╚══██╔══╝██╔═══██╗██╔═══██╗██║     
   ██║   ██║   ██║██║   ██║██║     
   ██║   ██║   ██║██║   ██║██║     
   ██║   ╚██████╔╝╚██████╔╝███████╗
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

██╗     ██╗███████╗████████╗
██║     ██║██╔════╝╚══██╔══╝
██║     ██║███████╗   ██║   
██║     ██║╚════██║   ██║   
███████╗██║███████║   ██║   
╚══════╝╚═╝╚══════╝   ╚═╝   

""", style="bold cyan")

        console.print("[1] Termux Tools")
        console.print("[2] Linux Tools")

        tool = input("\nChoose Category: ")

        if tool == "1":

            os.system("clear")

            console.print("""

████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝
   ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝ 
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗ 
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝

████████╗ ██████╗  ██████╗ ██╗     ███████╗
╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
   ██║   ██║   ██║██║   ██║██║     ███████╗
   ██║   ██║   ██║██║   ██║██║     ╚════██║
   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

""", style="bold green")

            console.print("[1] Git Tools")
            console.print("[2] Pkg Tools")
            console.print("[3] Dev Tools")
            console.print("[4] Hacking Tools")

            termux_tool = input("\nChoose Category: ")

            if termux_tool == "1":

                tools = data["termux"]["git_termux"]

            elif termux_tool == "2":

                tools = data["termux"]["pkg_termux"]

            elif termux_tool == "3":

                tools = data["termux"]["dev_termux"]

            elif termux_tool == "4":

                tools = data["termux"]["hacking_termux"]

            else:

                console.print("[bold red]Invalid Choice[/bold red]")
                input("Press Enter...")
                continue

        elif tool == "2":

            os.system("clear")

            console.print("""

██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗
██║     ██║████╗  ██║██║   ██║╚██╗██╔╝
██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝ 
██║     ██║██║╚██╗██║██║   ██║ ██╔██╗ 
███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗
╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝

████████╗ ██████╗  ██████╗ ██╗     ███████╗
╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
   ██║   ██║   ██║██║   ██║██║     ███████╗
   ██║   ██║   ██║██║   ██║██║     ╚════██║
   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

""", style="bold yellow")

            console.print("[1] Git Tools")
            console.print("[2] Apt Tools")
            console.print("[3] Dev Tools")
            console.print("[4] Hacking Tools")

            linux_tool = input("\nChoose Category: ")

            if linux_tool == "1":

                tools = data["linux"]["git_linux"]

            elif linux_tool == "2":

                tools = data["linux"]["apt_linuc"]

            elif linux_tool == "3":

                tools = data["linux"]["dev_linux"]

            elif linux_tool == "4":

                tools = data["linux"]["hacking_linux"]

            else:

                console.print("[bold red]Invalid Choice[/bold red]")
                input("Press Enter...")
                continue

        else:

            console.print("[bold red]Invalid Choice[/bold red]")
            input("Press Enter...")
            continue

        os.system("clear")

        console.print("\n[bold yellow]Available Tools:[/bold yellow]\n")

        colors = ["red", "green", "yellow", "blue", "magenta", "cyan"]

        i = 0

        for name in tools:

            console.print(
                f"[bold {colors[i % len(colors)]}]- {name}[/bold {colors[i % len(colors)]}]"
            )

            i += 1

        tool_name = input("\nType tool name to install: ").strip()

        if tool_name in tools:

            command = tools[tool_name]

            console.print(
                f"\n[bold green]Installing {tool_name}...[/bold green]"
            )

            os.system(command)

        else:

            console.print("[bold red]Tool not found[/bold red]")

        input("\nPress Enter to continue...")

    elif choice == "2":

        os.system("pkg update -y && pkg upgrade -y")

        input("\nPress Enter to continue...")

    elif choice == "3":

        console.print("\n[bold red]Exiting...[/bold red]")

        break

    else:

        console.print("\n[bold red]Invalid Choice[/bold red]")

        input("Press Enter...")
