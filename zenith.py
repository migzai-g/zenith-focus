import customtkinter as ctk
import tkinter as tk
import os, sys, random, json, platform
from datetime import datetime, date, timedelta

QUOTES = [
    ("I have always shook with fright before human beings.", "Dazai — No Longer Human"),
    ("Mine has been a life of much shame.", "Dazai — No Longer Human"),
    ("I am convinced that human life is filled with many pure, happy moments.", "Dazai — No Longer Human"),
    ("The weak fear happiness itself.", "Dazai — No Longer Human"),
    ("I felt as though even I had the right to be happy.", "Dazai — No Longer Human"),
    ("I am a dreamer. I know so little of real life.", "Dostoevsky — White Nights"),
    ("To love is to suffer and there can be no love otherwise.", "Dostoevsky — White Nights"),
    ("Was it a dream? How is it that one single hour can hold so much?", "Dostoevsky — White Nights"),
    ("No man knows till he has suffered from the night how sweet the morning can be.", "Stoker — Dracula"),
    ("We are in Transylvania, and Transylvania is not England.", "Stoker — Dracula"),
    ("I find no peace, and all my war is done.", "Petrarca — Canzoniere"),
    ("Alas, I know not what to do or say — my mind grows cold.", "Petrarca — Canzoniere"),
    ("In this world, is the destiny of mankind controlled by some transcendental entity?", "Miura — Berserk"),
    ("A dream... it was a long dream.", "Miura — Berserk"),
    ("Regret is the domain of those who have taken a wrong turn in life.", "Miura — Berserk"),
    ("Even if we painstakingly piece together something lost, it still won't be the original.", "Miura — Berserk"),
    ("I have always fought. Fighting was proof that I was alive.", "Miura — Berserk"),
    ("You have no enemies. No one has the right to hurt another.", "Yukimura — Vinland Saga"),
    ("A true warrior needs no sword.", "Yukimura — Vinland Saga"),
    ("There is no land more beautiful than the next one.", "Yukimura — Vinland Saga"),
    ("I mustn't run away. I mustn't run away.", "Evangelion — Shinji Ikari"),
    ("Nobody can justify their own existence through logic alone.", "Evangelion — Misato Katsuragi"),
    ("Humans cannot create anything from nothing. We are not God.", "Evangelion — Ritsuko Akagi"),
    ("The fate of destruction is also the joy of rebirth.", "Evangelion — SEELE"),
    ("Don't run. Face what you fear.", "Evangelion — Rei Ayanami"),
    ("Who are you? I'm me!", "Perfect Blue — Mima Kirigoe"),
    ("Reality is just a nuance.", "Perfect Blue — Rumi Hidaka"),
    ("I'm not the real thing anymore.", "Perfect Blue — Mima Kirigoe"),
    ("Have you seen the Yellow Sign?", "Chambers — The King in Yellow"),
    ("The tatters of the King must hide, there must the pallid mask reside.", "Chambers — The King in Yellow"),
    ("Sleep well, for your last sleep approaches.", "Chambers — The King in Yellow"),
    ("Along the shore the cloud waves break, the twin suns sink behind the lake.", "Chambers — The King in Yellow"),
]

THEMES = {
    "green":  {"label": "[ green ]",  "BG_BASE": "#0a0a0a", "BG_CARD": "#0f0f0f", "BG_CARD_END": "#0a1a08", "BG_ENTRY": "#141414",
               "MAIN": "#39ff14", "MAIN_DIM": "#1a7a08", "MAIN_MID": "#22cc0a", "TEXT_WHITE": "#e8e8e8",
               "TEXT_DIM": "#2e4a2e", "BORDER": "#1a2a1a", "LVL1": "#0d3a04", "LVL2": "#166608", "LVL3": "#1fa80d", "LVL4": "#2fd611"},
    "amber":  {"label": "[ amber ]",  "BG_BASE": "#0a0805", "BG_CARD": "#100d08", "BG_CARD_END": "#1a1206", "BG_ENTRY": "#161208",
               "MAIN": "#ffb000", "MAIN_DIM": "#8a5c00", "MAIN_MID": "#cc8c00", "TEXT_WHITE": "#f0e8d8",
               "TEXT_DIM": "#4a3a1e", "BORDER": "#2a2010", "LVL1": "#3a2a04", "LVL2": "#664c08", "LVL3": "#a8780d", "LVL4": "#d69e11"},
    "blood":  {"label": "[ blood ]",  "BG_BASE": "#0a0505", "BG_CARD": "#100808", "BG_CARD_END": "#1a0606", "BG_ENTRY": "#160a0a",
               "MAIN": "#ff2d2d", "MAIN_DIM": "#7a1414", "MAIN_MID": "#cc2222", "TEXT_WHITE": "#e8d8d8",
               "TEXT_DIM": "#4a2424", "BORDER": "#2a1414", "LVL1": "#3a0c0c", "LVL2": "#661414", "LVL3": "#a81d1d", "LVL4": "#d62929"},
    "cyan":   {"label": "[ cyan ]",   "BG_BASE": "#05090a", "BG_CARD": "#080e10", "BG_CARD_END": "#06181a", "BG_ENTRY": "#0a1214",
               "MAIN": "#1aeaff", "MAIN_DIM": "#0c6b7a", "MAIN_MID": "#14b8cc", "TEXT_WHITE": "#d8eef0",
               "TEXT_DIM": "#1e3a40", "BORDER": "#10282a", "LVL1": "#04303a", "LVL2": "#08596a", "LVL3": "#0d96a8", "LVL4": "#11c4d6"},
    "violet": {"label": "[ violet ]", "BG_BASE": "#08050a", "BG_CARD": "#0d0810", "BG_CARD_END": "#160a1a", "BG_ENTRY": "#100a14",
               "MAIN": "#b14aff", "MAIN_DIM": "#5c1f8a", "MAIN_MID": "#8c33cc", "TEXT_WHITE": "#e8d8f0",
               "TEXT_DIM": "#34204a", "BORDER": "#20142a", "LVL1": "#2a0c3a", "LVL2": "#4c1466", "LVL3": "#781da8", "LVL4": "#9c29d6"},
    "mono":   {"label": "[ mono ]",   "BG_BASE": "#0a0a0a", "BG_CARD": "#101010", "BG_CARD_END": "#1a1a1a", "BG_ENTRY": "#141414",
               "MAIN": "#e8e8e8", "MAIN_DIM": "#5a5a5a", "MAIN_MID": "#9a9a9a", "TEXT_WHITE": "#e8e8e8",
               "TEXT_DIM": "#3a3a3a", "BORDER": "#222222", "LVL1": "#2e2e2e", "LVL2": "#5a5a5a", "LVL3": "#8c8c8c", "LVL4": "#bcbcbc"},
}

IS_WINDOWS = platform.system() == "Windows"
MONO = "Consolas"


def heat_color(theme, count):
    if count == 0: return "#161616"
    if count == 1: return theme["LVL1"]
    if count == 2: return theme["LVL2"]
    if count <= 4: return theme["LVL3"]
    return theme["LVL4"]


def log_path():
    base = os.path.dirname(sys.executable) if getattr(sys, "frozen", False) else os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "zenith_log.json")


def settings_path():
    base = os.path.dirname(sys.executable) if getattr(sys, "frozen", False) else os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "zenith_settings.json")


def load_log():
    p = log_path()
    if not os.path.exists(p): return []
    try:
        with open(p, "r", encoding="utf-8") as f: return json.load(f)
    except Exception: return []


def save_log(entries):
    try:
        with open(log_path(), "w", encoding="utf-8") as f: json.dump(entries, f, ensure_ascii=False, indent=2)
    except Exception: pass


def load_settings():
    p = settings_path()
    default = {"theme": "green", "duration": "30"}
    if not os.path.exists(p): return default
    try:
        with open(p, "r", encoding="utf-8") as f:
            d = json.load(f)
            if d.get("theme") not in THEMES: d["theme"] = "green"
            if "duration" not in d: d["duration"] = "30"
            return d
    except Exception: return default


def save_settings(settings):
    try:
        with open(settings_path(), "w", encoding="utf-8") as f: json.dump(settings, f)
    except Exception: pass


def format_time(seconds):
    return f"{seconds // 60:02d}:{seconds % 60:02d}"


class ZenithApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        self.withdraw()
        
        if IS_WINDOWS:
            self._anchor = tk.Toplevel(self)
            self._anchor.title("Zenith Focus Hub")
            self._anchor.geometry("0x0+0+0")
            self._anchor.attributes("-alpha", 0.0)
            self._anchor.bind("<Map>", self._on_anchor_map)
            self._anchor.bind("<Unmap>", self._on_anchor_unmap)
        
        self.title("Zenith Focus Hub")
        self.resizable(True, True)
        self.minsize(820, 480)

        W, H = 1100, 600
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self._last_w, self._last_h = W, H
        self.geometry(f"{W}x{H}+{(sw-W)//2}+{(sh-H)//2}")

        self.settings = load_settings()
        self.theme_name = self.settings["theme"]
        self.theme = THEMES[self.theme_name]
        self.configure(fg_color=self.theme["BG_BASE"])

        self._drag_x = self._drag_y = 0
        self._resize_x = self._resize_y = 0
        self._resize_w = self._resize_h = 0
        
        self.pomodoro_minutes = int(self.settings["duration"])
        self.pomodoro_seconds = self.pomodoro_minutes * 60
        self.timer_running = False
        self.cycle_count = 0
        self._pinned = False
        self._quote, self._source = random.choice(QUOTES)
        self._log_entries = load_log()
        self._heat_cells = {}
        self._tooltip_win = None
        self._theme_menu = None
        self._restoring = False

        self._build_ui()
        self._bind_drag()
        
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self.after(1, self._init_window_state)

    def _init_window_state(self):
        self.deiconify()
        self._tick()

    def _minimize_window(self):
        if IS_WINDOWS:
            self._anchor.iconify()
        else:
            self.iconify()

    def _on_anchor_map(self, event):
        """Restauração instantânea sem remontar nada."""
        self._restoring = True
        self.deiconify()
        self.lift()
        self.after(50, self._reset_restoring_flag)

    def _reset_restoring_flag(self):
        self._restoring = False

    def _on_anchor_unmap(self, event):
        self.withdraw()

    def _on_close(self):
        if IS_WINDOWS:
            try: self._anchor.destroy()
            except Exception: pass
        self.destroy()

    def _build_ui(self):
        t = self.theme
        self._bar = ctk.CTkFrame(self, fg_color="#050505", height=28, corner_radius=0)
        self._bar.pack(fill="x")
        self._bar.pack_propagate(False)

        ctk.CTkLabel(self._bar, text="zenith://focus  v4.3", font=(MONO, 9), text_color=t["MAIN_DIM"]).pack(side="left", padx=14)
        self._bar_cycle = ctk.CTkLabel(self._bar, text="[cycles: 00]", font=(MONO, 8), text_color=t["TEXT_DIM"])
        self._bar_cycle.pack(side="left", padx=6)

        self._close_btn = ctk.CTkButton(self._bar, text="[x]", width=30, height=20, fg_color="transparent",
                                        hover_color="#2a1414", text_color=t["MAIN_DIM"], font=(MONO, 9),
                                        corner_radius=2, command=self._on_close)
        self._close_btn.pack(side="right", padx=4)

        self._minimize_btn = ctk.CTkButton(self._bar, text="[_]", width=30, height=20, fg_color="transparent",
                                           hover_color="#101010", text_color=t["MAIN_DIM"], font=(MONO, 9),
                                           corner_radius=2, command=self._minimize_window)
        self._minimize_btn.pack(side="right", padx=2)

        self._pin_btn = ctk.CTkButton(self._bar, text="[pin]", width=38, height=20, fg_color="transparent",
                                      hover_color="#0a1a0a", text_color=t["TEXT_DIM"], font=(MONO, 9),
                                      corner_radius=2, command=self._toggle_pin)
        self._pin_btn.pack(side="right", padx=2)

        self._theme_btn = ctk.CTkButton(self._bar, text=t["label"], width=68, height=20, fg_color="transparent",
                                        hover_color="#101010", text_color=t["MAIN_DIM"], font=(MONO, 9),
                                        corner_radius=2, command=self._show_theme_menu)
        self._theme_btn.pack(side="right", padx=2)

        g = ctk.CTkFrame(self, fg_color=t["BG_BASE"])
        g.pack(fill="both", expand=True, padx=8, pady=(0, 8))
        g.columnconfigure(0, weight=2, minsize=200)
        g.columnconfigure(1, weight=3, minsize=260)
        g.columnconfigure(2, weight=4, minsize=360)
        g.rowconfigure(0, weight=1)

        c0 = self._card(g, 0, 0)
        c1 = self._card(g, 0, 1)
        c2 = self._card(g, 0, 2)

        self._build_pomodoro(c0)
        self._build_quotes(c1)
        self._build_log_and_heat(c2)

        grip = ctk.CTkLabel(self, text="◢", font=(MONO, 12), text_color=t["TEXT_DIM"], fg_color=t["BG_BASE"], cursor="sizing")
        grip.place(relx=1.0, rely=1.0, anchor="se")
        grip.bind("<ButtonPress-1>", self._resize_start)
        grip.bind("<B1-Motion>", self._resize_move)

    def _card(self, parent, row, col):
        t = self.theme
        f = ctk.CTkFrame(parent, fg_color=t["BG_CARD"], border_color=t["BORDER"], border_width=1, corner_radius=4)
        f.grid(row=row, column=col, sticky="nsew", padx=6, pady=6)
        return f

    def _build_pomodoro(self, parent):
        t = self.theme
        self._pcard_ref = parent
        
        lbl = ctk.CTkLabel(parent, text="// pomodoro.timer   ", font=(MONO, 10, "bold"), text_color=t["TEXT_DIM"])
        lbl.pack(pady=(14, 6))

        opt_frame = ctk.CTkFrame(parent, fg_color="transparent")
        opt_frame.pack(pady=2)

        self._time_menu = ctk.CTkOptionMenu(opt_frame, values=["10 min", "25 min", "30 min", "45 min", "60 min"],
                                            command=self._change_timer_duration, font=(MONO, 9), dropdown_font=(MONO, 9),
                                            width=85, height=20, fg_color=t["BG_ENTRY"], button_color=t["BORDER"],
                                            button_hover_color=t["BG_BASE"], text_color=t["MAIN"], 
                                            dropdown_fg_color=t["BG_CARD"], dropdown_text_color=t["MAIN"])
        self._time_menu.set(f"{self.pomodoro_minutes} min")
        self._time_menu.pack()

        self._time_label = ctk.CTkLabel(parent, text=format_time(self.pomodoro_seconds), font=(MONO, 38, "bold"), text_color=t["MAIN"])
        self._time_label.pack(pady=10)

        self._progress = ctk.CTkProgressBar(parent, width=150, height=4, corner_radius=0, fg_color="#121212", progress_color=t["MAIN_DIM"])
        self._progress.set(1.0)
        self._progress.pack(pady=10)

        b_frame = ctk.CTkFrame(parent, fg_color="transparent")
        b_frame.pack(pady=14)

        self._start_btn = ctk.CTkButton(b_frame, text="[start]", width=54, height=24, fg_color="transparent",
                                        hover_color="#101010", text_color=t["TEXT_WHITE"], font=(MONO, 10),
                                        corner_radius=2, command=self._start_timer)
        self._start_btn.pack(side="left", padx=4)

        self._pause_btn = ctk.CTkButton(b_frame, text="[pause]", width=54, height=24, fg_color="transparent",
                                        hover_color="#101010", text_color=t["TEXT_DIM"], font=(MONO, 10),
                                        corner_radius=2, command=self._pause_timer)
        self._pause_btn.pack(side="left", padx=4)

        self._reset_btn = ctk.CTkButton(b_frame, text="[skip]", width=48, height=24, fg_color="transparent",
                                        hover_color="#101010", text_color=t["TEXT_DIM"], font=(MONO, 10),
                                        corner_radius=2, command=self._skip_timer)
        self._reset_btn.pack(side="left", padx=4)

    def _build_quotes(self, parent):
        t = self.theme
        self._quote_card_ref = parent
        
        h_frame = ctk.CTkFrame(parent, fg_color="transparent")
        h_frame.pack(pady=(14, 6), fill="x")
        
        ctk.CTkLabel(h_frame, text="// thoughts   ", font=(MONO, 10, "bold"), text_color=t["TEXT_DIM"]).pack(side="left", expand=True, padx=(24, 0))
        
        self._roll_btn = ctk.CTkButton(h_frame, text="[↻]", width=20, height=18, fg_color="transparent",
                                       hover_color="#141414", text_color=t["MAIN_DIM"], font=(MONO, 10),
                                       corner_radius=2, command=self._roll_quote)
        self._roll_btn.pack(side="right", padx=10)

        self._quote_label = ctk.CTkLabel(parent, text=f'"{self._quote}"', font=(MONO, 11, "italic"),
                                         text_color=t["TEXT_WHITE"], wraplength=220, justify="center")
        self._quote_label.pack(expand=True, padx=16, pady=4)

        self._quote_sep = ctk.CTkFrame(parent, height=1, width=60, fg_color=t["BORDER"])
        self._quote_sep.pack(pady=4)

        self._source_label = ctk.CTkLabel(parent, text=self._source, font=(MONO, 9), text_color=t["MAIN_DIM"])
        self._source_label.pack(pady=(2, 14))

    def _build_log_and_heat(self, parent):
        t = self.theme
        self._log_card = parent

        top = ctk.CTkFrame(parent, fg_color="transparent", height=24)
        top.pack(fill="x", padx=10, pady=(10, 4))
        
        ctk.CTkLabel(top, text="// logs   ", font=(MONO, 10, "bold"), text_color=t["TEXT_DIM"]).pack(side="left")
        self._log_count_lbl = ctk.CTkLabel(top, text=f"({len(self._log_entries)} ops)", font=(MONO, 9), text_color=t["TEXT_DIM"])
        self._log_count_lbl.pack(side="left", padx=6)

        self._log_scroll = ctk.CTkScrollableFrame(parent, fg_color=t["BG_CARD"], corner_radius=0,
                                                  scrollbar_button_color=t["MAIN_DIM"],
                                                  scrollbar_button_hover_color=t["MAIN_MID"],
                                                  scrollbar_fg_color=t["BG_CARD"])
        self._log_scroll.pack(fill="both", expand=True, padx=10, pady=4)
        self._render_log_list()

        h_frame = ctk.CTkFrame(parent, fg_color="transparent", height=115)
        h_frame.pack(fill="x", padx=10, pady=(4, 10))
        h_frame.pack_propagate(False)

        self._heat_canvas = tk.Canvas(h_frame, bg=t["BG_CARD"], bd=0, highlightthickness=0, height=72)
        self._heat_canvas.pack(fill="x", pady=(2, 0))
        self._heat_canvas.bind("<Motion>", self._heat_hover)
        self._heat_canvas.bind("<Leave>", self._heat_leave)

        self._month_canvas = tk.Canvas(h_frame, bg=t["BG_CARD"], bd=0, highlightthickness=0, height=14)
        self._month_canvas.pack(fill="x")

        self._legend_frame = ctk.CTkFrame(h_frame, fg_color="transparent", height=14)
        self._legend_frame.pack(fill="x", pady=(2, 0))
        
        self._draw_heatmap()
        self._build_legend()

    def _change_timer_duration(self, choice):
        if self.timer_running:
            self._pause_timer()
        self.pomodoro_minutes = int(choice.split()[0])
        self.pomodoro_seconds = self.pomodoro_minutes * 60
        self._time_label.configure(text=format_time(self.pomodoro_seconds))
        self._progress.set(1.0)
        self.settings["duration"] = str(self.pomodoro_minutes)
        save_settings(self.settings)

    def _roll_quote(self):
        self._quote, self._source = random.choice(QUOTES)
        self._quote_label.configure(text=f'"{self._quote}"')
        self._source_label.configure(text=self._source)

    def _render_log_list(self):
        for w in self._log_scroll.winfo_children(): w.destroy()
        t = self.theme
        for i, item in enumerate(reversed(self._log_entries)):
            f = ctk.CTkFrame(self._log_scroll, fg_color="transparent", height=20)
            f.pack(fill="x", pady=2)
            f.pack_propagate(False)

            lbl_t = ctk.CTkLabel(f, text=item["time"], font=(MONO, 9), text_color=t["MAIN_DIM"])
            lbl_t.pack(side="left")

            lbl_m = ctk.CTkLabel(f, text=f" {item['msg']}", font=(MONO, 10), text_color=t["TEXT_WHITE"], anchor="w")
            lbl_m.pack(side="left", fill="x", expand=True)

            btn = ctk.CTkButton(f, text="[x]", width=18, height=16, fg_color="transparent",
                                hover_color="#201010", text_color=t["TEXT_DIM"], font=(MONO, 8), corner_radius=2)
            btn.pack(side="right", padx=2)
            idx_in_orig = len(self._log_entries) - 1 - i
            btn.configure(command=lambda idx=idx_in_orig: self._delete_log(idx))

    def _build_legend(self):
        for w in self._legend_frame.winfo_children(): w.destroy()
        t = self.theme
        ctk.CTkLabel(self._legend_frame, text="less ", font=(MONO, 8), text_color=t["TEXT_DIM"]).pack(side="left")
        for count in [0, 1, 2, 4, 8]:
            lbl = ctk.CTkLabel(self._legend_frame, text="■", font=(MONO, 9), text_color=heat_color(t, count))
            lbl.pack(side="left", padx=1)
        ctk.CTkLabel(self._legend_frame, text=" more", font=(MONO, 8), text_color=t["TEXT_DIM"]).pack(side="left")

    def _heat_hover(self, event):
        x, y = event.x, event.y
        matched = None
        for (r, c), info in self._heat_cells.items():
            x1, y1, x2, y2 = info["coords"]
            if x1 <= x <= x2 and y1 <= y <= y2:
                matched = info
                break
        if matched:
            txt = f"{matched['date']}: {matched['count']} sessions"
            if not self._tooltip_win:
                self._tooltip_win = tk.Toplevel(self)
                self._tooltip_win.wm_overrideredirect(True)
                self._tooltip_win.attributes("-topmost", True)
                self._tooltip_lbl = tk.Label(self._tooltip_win, font=(MONO, 9), bg="#121212", fg="#ffffff", padx=6, pady=3, bd=1, relief="solid")
                self._tooltip_lbl.pack()
            self._tooltip_lbl.configure(text=txt, fg=self.theme["MAIN"])
            self._tooltip_win.wm_geometry(f"{self._tooltip_lbl.winfo_reqwidth()}x{self._tooltip_lbl.winfo_reqheight()}+{event.x_root + 12}+{event.y_root + 12}")
        else:
            self._heat_leave(None)

    def _heat_leave(self, event):
        if self._tooltip_win:
            self._tooltip_win.destroy()
            self._tooltip_win = None

    def _draw_heatmap(self):
        """Buffer de desenho rápido - Otimizado contra flickers"""
        canvas = self._heat_canvas
        m_canvas = self._month_canvas
        canvas.delete("all")
        m_canvas.delete("all")
        
        t = self.theme
        self._heat_cells = {}
        counts = {}
        for entry in self._log_entries:
            d_str = entry.get("date", "")
            if d_str: counts[d_str] = counts.get(d_str, 0) + 1

        end_date = date.today()
        start_date = end_date - timedelta(days=174)
        current = start_date
        while current.weekday() != 6: current -= timedelta(days=1)

        columns, col_days = [], []
        while current <= end_date:
            col_days.append(current)
            if len(col_days) == 7:
                columns.append(col_days)
                col_days = []
            current += timedelta(days=1)
        if col_days:
            while len(col_days) < 7: col_days.append(None)
            columns.append(col_days)

        box_w, box_h, gap = 9, 9, 2
        
        # Batch drawing para aceleração tcl/tk
        for c_idx, col in enumerate(columns):
            first_day_of_col = col[0]
            if first_day_of_col and first_day_of_col.day <= 7:
                m_canvas.create_text(c_idx * (box_w + gap), 8, text=first_day_of_col.strftime("%b").lower(), anchor="w", fill=t["TEXT_DIM"], font=(MONO, 8))

            for r_idx, day in enumerate(col):
                if not day: continue
                d_str = day.isoformat()
                cnt = counts.get(d_str, 0)
                x1, y1 = c_idx * (box_w + gap), r_idx * (box_h + gap)
                x2, y2 = x1 + box_w, y1 + box_h
                canvas.create_rectangle(x1, y1, x2, y2, fill=heat_color(t, cnt), outline="")
                self._heat_cells[(r_idx, c_idx)] = {"coords": (x1, y1, x2, y2), "date": d_str, "count": cnt}

    def _bind_drag(self):
        self._bar.bind("<ButtonPress-1>", self._drag_start)
        self._bar.bind("<B1-Motion>", self._drag_move)

    def _drag_start(self, event):
        self._drag_x = event.x_root - self.winfo_x()
        self._drag_y = event.y_root - self.winfo_y()

    def _drag_move(self, event):
        self.geometry(f"+{event.x_root - self._drag_x}+{event.y_root - self._drag_y}")

    def _resize_start(self, event):
        self._resize_x, self._resize_y = event.x_root, event.y_root
        self._resize_w, self._resize_h = self.winfo_width(), self.winfo_height()

    def _resize_move(self, event):
        nw = max(820, self._resize_w + (event.x_root - self._resize_x))
        nh = max(480, self._resize_h + (event.y_root - self._resize_y))
        if nw != self._last_w or nh != self._last_h:
            self.geometry(f"{nw}x{nh}")
            self._last_w, self._last_h = nw, nh
            self._draw_heatmap()

    def _toggle_pin(self):
        self._pinned = not self._pinned
        self.attributes("-topmost", self._pinned)
        self._pin_btn.configure(text_color=self.theme["MAIN"] if self._pinned else self.theme["TEXT_DIM"])

    def _start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            if self.pomodoro_seconds == 0:
                self.pomodoro_seconds = self.pomodoro_minutes * 60
            self._start_btn.configure(text_color=self.theme["MAIN"])
            self._pause_btn.configure(text_color=self.theme["TEXT_DIM"])

    def _pause_timer(self):
        if self.timer_running:
            self.timer_running = False
            self._start_btn.configure(text_color=self.theme["TEXT_DIM"])
            self._pause_btn.configure(text_color=self.theme["MAIN"])

    def _skip_timer(self):
        self.timer_running = False
        self.pomodoro_seconds = self.pomodoro_minutes * 60
        self._time_label.configure(text=format_time(self.pomodoro_seconds))
        self._progress.set(1.0)
        self._pcard_ref.configure(fg_color=self.theme["BG_CARD"])
        self._start_btn.configure(text_color=self.theme["TEXT_WHITE"])
        self._pause_btn.configure(text_color=self.theme["TEXT_DIM"])

    def _tick(self):
        if self.timer_running and self.pomodoro_seconds > 0:
            self.pomodoro_seconds -= 1
            self._time_label.configure(text=format_time(self.pomodoro_seconds))
            self._progress.set(self.pomodoro_seconds / (self.pomodoro_minutes * 60))
            
            if self.pomodoro_seconds == 0:
                self.timer_running = False
                self.cycle_count += 1
                self._bar_cycle.configure(text=f"[cycles: {self.cycle_count:02d}]")
                self._pcard_ref.configure(fg_color=self.theme["BG_CARD_END"])
                self._start_btn.configure(text_color=self.theme["TEXT_DIM"])
                self._pause_btn.configure(text_color=self.theme["TEXT_DIM"])
                
                try:
                    self.attributes("-topmost", True)
                    self.attributes("-topmost", self._pinned)
                except Exception: pass
                
                self._prompt_log_entry()
        self.after(1000, self._tick)

    def _prompt_log_entry(self):
        t = self.theme
        box = tk.Toplevel(self)
        box.wm_overrideredirect(True)
        box.attributes("-topmost", True)
        box.configure(bg=t["BG_BASE"], bd=1, relief="solid", highlightbackground=t["BORDER"])
        
        bx = self.winfo_rootx() + (self.winfo_width() - 320) // 2
        by = self.winfo_rooty() + (self.winfo_height() - 120) // 2
        box.geometry(f"320x120+{bx}+{by}")

        ctk.CTkLabel(box, text="--- CYCLE COMPLETE ---", font=(MONO, 10, "bold"), text_color=t["MAIN"]).pack(pady=(10, 4))
        ctk.CTkLabel(box, text="What did you focus on during this session?", font=(MONO, 9), text_color=t["TEXT_WHITE"]).pack()

        entry_frame = ctk.CTkFrame(box, height=28, fg_color="transparent", border_width=1, border_color=t["MAIN_DIM"], corner_radius=3)
        entry_frame.pack(fill="x", padx=15, pady=8)
        entry_frame.pack_propagate(False)

        ent = ctk.CTkEntry(entry_frame, placeholder_text="descriptor...", font=(MONO, 10), fg_color=t["BG_ENTRY"], text_color=t["MAIN"], border_width=0, corner_radius=0)
        ent.pack(side="left", fill="both", expand=True, padx=2, pady=2)
        ent.focus_set()

        def submit():
            val = ent.get().strip() or "Unspecified Focus Session"
            now = datetime.now()
            self._log_entries.append({"time": now.strftime("%H:%M"), "date": date.today().isoformat(), "msg": f"[{self.pomodoro_minutes}m] {val}"})
            save_log(self._log_entries)
            self._log_count_lbl.configure(text=f"({len(self._log_entries)} ops)")
            self._render_log_list()
            self._draw_heatmap()
            self._pcard_ref.configure(fg_color=t["BG_CARD"])
            self._skip_timer()
            box.destroy()

        ent.bind("<Return>", lambda e: submit())

    def _delete_log(self, idx):
        if 0 <= idx < len(self._log_entries):
            self._log_entries.pop(idx)
            save_log(self._log_entries)
            self._log_count_lbl.configure(text=f"({len(self._log_entries)} ops)")
            self._render_log_list()
            self._draw_heatmap()

    def _show_theme_menu(self):
        if self._theme_menu:
            self._theme_menu.destroy()
            self._theme_menu = None
            return
        t = self.theme
        m = tk.Toplevel(self)
        m.wm_overrideredirect(True)
        m.attributes("-topmost", True)
        m.configure(bg="#0a0a0a", bd=1, relief="solid", highlightbackground=t["BORDER"])
        self._theme_menu = m
        m.wm_geometry(f"90x{len(THEMES)*22}+{self._theme_btn.winfo_rootx()}+{self._theme_btn.winfo_rooty()+self._theme_btn.winfo_height()+2}")

        for name, info in THEMES.items():
            tk.Button(m, text=f" {info['label']}", font=(MONO, 9), anchor="w", bg="#0a0a0a", fg=info["MAIN_DIM"], bd=0,
                      activebackground="#161616", activeforeground=info["MAIN"], command=lambda n=name: self._change_theme(n)).pack(fill="x")
        m.bind("<FocusOut>", lambda e: self._close_theme_menu())
        m.focus_set()

    def _close_theme_menu(self):
        if self._theme_menu:
            self._theme_menu.after(10, self._theme_menu.destroy)
            self._theme_menu = None

    def _change_theme(self, name):
        if name in THEMES:
            self.theme_name = name
            self.theme = THEMES[name]
            self.settings["theme"] = name
            save_settings(self.settings)
            self._apply_theme()
        self._close_theme_menu()

    def _apply_theme(self):
        t = self.theme
        self.configure(fg_color=t["BG_BASE"])
        self._theme_btn.configure(text=t["label"], text_color=t["MAIN_DIM"])
        self._close_btn.configure(text_color=t["MAIN_DIM"])
        self._minimize_btn.configure(text_color=t["MAIN_DIM"])
        
        for card in [self._pcard_ref, self._quote_card_ref, self._log_card]:
            if card: card.configure(fg_color=t["BG_CARD"], border_color=t["BORDER"])

        self._time_label.configure(text_color=t["MAIN"])
        self._progress.configure(progress_color=t["MAIN_DIM"])
        self._pcard_ref.configure(fg_color=t["BG_CARD_END"] if self.pomodoro_seconds == 0 else t["BG_CARD"])
        self._quote_label.configure(text_color=t["TEXT_WHITE"])
        self._source_label.configure(text_color=t["MAIN_DIM"])
        self._quote_sep.configure(fg_color=t["BORDER"])
        self._roll_btn.configure(text_color=t["MAIN_DIM"])
        self._log_count_lbl.configure(text_color=t["TEXT_DIM"])
        
        self._time_menu.configure(fg_color=t["BG_ENTRY"], button_color=t["BORDER"], text_color=t["MAIN"],
                                  font=(MONO, 9), dropdown_font=(MONO, 9))
        
        self._log_scroll.configure(fg_color=t["BG_CARD"], scrollbar_button_color=t["MAIN_DIM"], scrollbar_fg_color=t["BG_CARD"])
        self._heat_canvas.configure(bg=t["BG_CARD"])
        self._month_canvas.configure(bg=t["BG_CARD"])
        self._draw_heatmap()
        self._build_legend()
        self._pin_btn.configure(text_color=t["MAIN"] if self._pinned else t["TEXT_DIM"])


if __name__ == "__main__":
    app = ZenithApp()
    app.mainloop()