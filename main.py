import curses
import time
from windfall import Windfall
from core import NodeScanner
from branding import THEMES, LOGO_ANSI

class VemberDashboard:
    def __init__(self):
        self.scanner = NodeScanner()
        # Initialize the Compositor with our default theme
        self.windfall = Windfall(theme_key="VEMBER_DARK")
        
        self.selected_index = 0
        self.running = True
        self.nodes = []

    def show_splash(self, stdscr):
        """Initial Boot Sequence (Point 7 of Checklist)"""
        stdscr.erase()
        h, w = stdscr.getmaxyx()
        
        # Simple center-screen splash using branding assets
        logo_lines = LOGO_ANSI.splitlines()
        start_y = (h // 2) - (len(logo_lines) // 2)
        
        for i, line in enumerate(logo_lines):
            if start_y + i < h:
                stdscr.addstr(start_y + i, (w // 2) - (len(line) // 2), line)
        
        stdscr.refresh()
        time.sleep(1.5) # Let the brand sink in

    def update_logic(self, key):
        """Pure Logic: No Rendering allowed here."""
        self.nodes = self.scanner.scan()
        num_nodes = len(self.nodes)

        if key == ord('q'):
            self.running = False
        # Toggles handled by the OS, passed to Windfall (Point 2)
        elif key == curses.KEY_F1:
            self.windfall.toggle_sidebar()
        elif key == curses.KEY_F2:
            self.windfall.toggle_inspector()
        elif key == curses.KEY_UP and self.selected_index > 0:
            self.selected_index -= 1
        elif key == curses.KEY_DOWN and self.selected_index < num_nodes - 1:
            self.selected_index += 1

    def _get_sidebar_content(self):
        """Component for Windfall: Formats the node list."""
        content = ""
        for i, node in enumerate(self.nodes):
            prefix = "▶ " if i == self.selected_index else "  "
            line = f"{prefix}{node['display_name']}"
            if i == self.selected_index:
                content += f"[bold cyan]{line}[/]\n"
            else:
                content += f"{line}\n"
        return content

    def _get_inspector_content(self):
        """Component for Windfall: Formats node details."""
        if not self.nodes:
            return "[dim]Scanning /ops...[/]"
        curr = self.nodes[self.selected_index]
        return f"[yellow]ID:[/] {curr['id']}\n[yellow]SRC:[/] {curr['path']}\n\n{curr['description']}"

    def _get_footer_content(self):
        """Component for Windfall: Keybind help."""
        return "[dim]ARROWS Navigate | ENTER Run | F1 Sidebar | F2 Inspector | Q Quit[/]"

    def run(self, stdscr):
        """The Main Ncurses Loop."""
        self.show_splash(stdscr) # Point 7: Boot Sequence
        
        curses.curs_set(0)
        stdscr.nodelay(True)
        stdscr.keypad(True)

        while self.running:
            # 1. Update State & Dimensions (Point 6: Responsive)
            key = stdscr.getch()
            self.update_logic(key)
            h, w = stdscr.getmaxyx()

            # 2. Compose the Frame (Point 3: Frame-based Rendering)
            # We pass callables so Windfall only runs them if the panel is visible
            frame = self.windfall.compose(w, h, {
                "sidebar": self._get_sidebar_content,
                "inspector": self._get_inspector_content,
                "footer": self._get_footer_content
            })
            
            # 3. Paint the Compositor Output
            stdscr.erase()
            try:
                for y, line in enumerate(frame.splitlines()):
                    if y < h:
                        stdscr.addstr(y, 0, line.rstrip()[:w-1])
            except curses.error:
                pass

            stdscr.refresh()
            time.sleep(0.05)

if __name__ == "__main__":
    app = VemberDashboard()
    curses.wrapper(app.run)