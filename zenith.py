

QUOTES = [
    # ── Osamu Dazai — No Longer Human
    ("I have always shook with fright before human beings.", "Dazai — No Longer Human"),
    ("Mine has been a life of much shame.", "Dazai — No Longer Human"),
    ("I am convinced that human life is filled with many pure, happy moments.", "Dazai — No Longer Human"),
    ("The weak fear happiness itself.", "Dazai — No Longer Human"),
    ("I felt as though even I had the right to be happy.", "Dazai — No Longer Human"),

    # ── Fyodor Dostoevsky — White Nights
    ("I am a dreamer. I know so little of real life.", "Dostoevsky — White Nights"),
    ("To love is to suffer and there can be no love otherwise.", "Dostoevsky — White Nights"),
    ("Was it a dream? How is it that one single hour can hold so much?", "Dostoevsky — White Nights"),

    # ── Bram Stoker — Dracula
    ("No man knows till he has suffered from the night how sweet the morning can be.", "Stoker — Dracula"),
    ("We are in Transylvania, and Transylvania is not England.", "Stoker — Dracula"),

    # ── Petrarca — Canzoniere
    ("I find no peace, and all my war is done.", "Petrarca — Canzoniere"),
    ("Alas, I know not what to do or say — my mind grows cold.", "Petrarca — Canzoniere"),

    # ── Kentaro Miura — Berserk
    ("In this world, is the destiny of mankind controlled by some transcendental entity?", "Miura — Berserk"),
    ("A dream... it was a long dream.", "Miura — Berserk"),
    ("Regret is the domain of those who have taken a wrong turn in life.", "Miura — Berserk"),
    ("Even if we painstakingly piece together something lost, it still won't be the original.", "Miura — Berserk"),
    ("I have always fought. Fighting was proof that I was alive.", "Miura — Berserk"),

    # ── Makoto Yukimura — Vinland Saga
    ("You have no enemies. No one has the right to hurt another.", "Yukimura — Vinland Saga"),
    ("A true warrior needs no sword.", "Yukimura — Vinland Saga"),
    ("There is no land more beautiful than the next one.", "Yukimura — Vinland Saga"),

    # ── Neon Genesis Evangelion
    ("I mustn't run away. I mustn't run away.", "Evangelion — Shinji Ikari"),
    ("Nobody can justify their own existence through logic alone.", "Evangelion — Misato Katsuragi"),
    ("Humans cannot create anything from nothing. We are not God.", "Evangelion — Ritsuko Akagi"),
    ("The fate of destruction is also the joy of rebirth.", "Evangelion — SEELE"),
    ("Don't run. Face what you fear.", "Evangelion — Rei Ayanami"),

    # ── Perfect Blue
    ("Who are you? I'm me!", "Perfect Blue — Mima Kirigoe"),
    ("Reality is just a nuance.", "Perfect Blue — Rumi Hidaka"),
    ("I'm not the real thing anymore.", "Perfect Blue — Mima Kirigoe"),

    # ── The King in Yellow — Robert W. Chambers
    ("Have you seen the Yellow Sign?", "Chambers — The King in Yellow"),
    ("The tatters of the King must hide, there must the pallid mask reside.", "Chambers — The King in Yellow"),
    ("Sleep well, for your last sleep approaches.", "Chambers — The King in Yellow"),
    ("Along the shore the cloud waves break, the twin suns sink behind the lake.", "Chambers — The King in Yellow"),
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
import customtkinter as ctk
import tkinter as tk
import os, sys, random, json
from datetime import datetime, date, timedelta
from collections import defaultdict

BG_BASE      = "#0a0a0a"
BG_CARD      = "#0f0f0f"
BG_CARD_END  = "#0a1a08"
BG_ENTRY     = "#141414"
GREEN        = "#39ff14"
GREEN_DIM    = "#1a7a08"
GREEN_MID    = "#22cc0a"
GREEN_DARK   = "#0d4004"
AMBER        = "#b8a070"
TEXT_WHITE   = "#e8e8e8"
TEXT_DIM     = "#2e4a2e"
BORDER       = "#1a2a1a"
MONO         = "Consolas"
POMODORO_MINUTES = 30

HEAT_EMPTY = "#161616"
HEAT_L1    = "#0d3a04"
HEAT_L2    = "#166608"
HEAT_L3    = "#1fa80d"
HEAT_L4    = "#2fd611"
HEAT_MAX   = "#39ff14"

def heat_color(count):
    if count == 0:  return HEAT_EMPTY
    if count == 1:  return HEAT_L1
    if count == 2:  return HEAT_L2
    if count <= 4:  return HEAT_L3
    if count <= 8:  return HEAT_L4
    return HEAT_MAX


def log_path():
    if getattr(sys, "frozen", False):
        base = os.path.dirname(sys.executable)
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "zenith_log.json")

def load_log():
    p = log_path()
    if not os.path.exists(p):
        return []
    try:
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_log(entries):
    try:
        with open(log_path(), "w", encoding="utf-8") as f:
            json.dump(entries, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

def entries_per_day(entries):
    counts = defaultdict(int)
    for e in entries:
        try:
            day = e["time"].split(" - ")[0]
            counts[day] += 1
        except Exception:
            pass
    return counts

def fmt_time(s):
    return f"{s // 60:02d}:{s % 60:02d}"

def now_stamp():
    return datetime.now().strftime("%d/%m - %H:%M")

def day_key(d: date):
    return d.strftime("%d/%m")


class ZenithApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.update()

        self.title("Zenith Focus Hub")
        self.configure(fg_color=BG_BASE)
        self.resizable(True, True)
        self.minsize(820, 480)

        W, H = 1100, 600
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"{W}x{H}+{(sw-W)//2}+{(sh-H)//2}")
        self.after(50, self._remove_titlebar)

        self._drag_x = self._drag_y = 0
        self._resize_x = self._resize_y = 0
        self._resize_w = self._resize_h = 0
        self.pomodoro_seconds = POMODORO_MINUTES * 60
        self.timer_running = False
        self.cycle_count = 0
        self._pinned = False
        self._cursor_visible = True
        self._quote, self._source = random.choice(QUOTES)
        self._log_entries = load_log()
        self._awaiting_log = False
        self._heat_cells = {}
        self._tooltip_win = None

        self._build_ui()
        self._bind_drag()
        self._tick()
        self._blink_cursor()

    def _remove_titlebar(self):
        try:
            import ctypes
            hwnd = self.winfo_id()
            GWL_STYLE     = -16
            WS_CAPTION    = 0x00C00000
            WS_THICKFRAME = 0x00040000
            WS_MINIMIZEBOX= 0x00020000
            WS_SYSMENU    = 0x00080000
            SWP_FLAGS     = 0x0002|0x0001|0x0004|0x0020
            style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)
            style = (style & ~WS_CAPTION & ~WS_THICKFRAME) | WS_MINIMIZEBOX | WS_SYSMENU
            ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style)
            ctypes.windll.user32.SetWindowPos(hwnd, 0, 0, 0, 0, 0, SWP_FLAGS)
        except Exception:
            pass

    def _build_ui(self):
        self._bar = ctk.CTkFrame(self, fg_color="#050505", height=28, corner_radius=0)
        self._bar.pack(fill="x")
        self._bar.pack_propagate(False)

        ctk.CTkLabel(self._bar, text="zenith://focus  v4.1",
                     font=(MONO, 9), text_color=GREEN_DIM).pack(side="left", padx=14)
        self._bar_cycle = ctk.CTkLabel(self._bar, text="[cycles: 00]",
                                       font=(MONO, 8), text_color=TEXT_DIM)
        self._bar_cycle.pack(side="left", padx=6)

        ctk.CTkButton(self._bar, text="[x]", width=30, height=20,
                      fg_color="transparent", hover_color="#1a0808",
                      text_color=GREEN_DIM, font=(MONO, 9),
                      corner_radius=2, command=self.destroy).pack(side="right", padx=4)
        ctk.CTkButton(self._bar, text="[_]", width=30, height=20,
                      fg_color="transparent", hover_color="#0a1a0a",
                      text_color=GREEN_DIM, font=(MONO, 9),
                      corner_radius=2, command=self.iconify).pack(side="right", padx=2)
        self._pin_btn = ctk.CTkButton(self._bar, text="[pin]", width=38, height=20,
                                      fg_color="transparent", hover_color="#0a1a0a",
                                      text_color=TEXT_DIM, font=(MONO, 9),
                                      corner_radius=2, command=self._toggle_pin)
        self._pin_btn.pack(side="right", padx=2)

        g = ctk.CTkFrame(self, fg_color=BG_BASE)
        g.pack(fill="both", expand=True, padx=8, pady=(0, 8))
        g.columnconfigure(0, weight=2, minsize=190)
        g.columnconfigure(1, weight=3, minsize=260)
        g.columnconfigure(2, weight=4, minsize=360)
        g.rowconfigure(0, weight=1)

        c0 = self._card(g, 0, 0, pad=(0, 5))
        c1 = self._card(g, 0, 1, pad=(0, 5))
        c2 = self._card(g, 0, 2, pad=(0, 0))

        self._build_pomodoro(c0)
        self._build_quotes(c1)
        self._build_log_and_heat(c2)

        grip = ctk.CTkLabel(self, text="◢", font=(MONO, 12),
                            text_color=TEXT_DIM, fg_color=BG_BASE, cursor="sizing")
        grip.place(relx=1.0, rely=1.0, anchor="se")
        grip.bind("<ButtonPress-1>", self._resize_start)
        grip.bind("<B1-Motion>", self._resize_move)

    def _card(self, parent, row, col, pad=(0, 0)):
        c = ctk.CTkFrame(parent, fg_color=BG_CARD, corner_radius=6,
                         border_width=1, border_color=BORDER)
        c.grid(row=row, column=col, sticky="nsew", padx=pad, pady=0)
        c.grid_propagate(True)
        return c

    # ── Card 1: Pomodoro ──────────────────────────────────
    def _build_pomodoro(self, card):
        self._pcard_ref = card
        for i in range(5):
            card.rowconfigure(i, weight=1 if i == 1 else 0)
        card.columnconfigure(0, weight=1)

        ctk.CTkLabel(card, text="// pomodoro.timer",
                     font=(MONO, 9), text_color=GREEN_DIM,
                     anchor="w").grid(row=0, column=0, sticky="ew", padx=12, pady=(10, 0))

        self._time_label = ctk.CTkLabel(card, text=fmt_time(self.pomodoro_seconds),
                                        font=(MONO, 58, "bold"), text_color=GREEN,
                                        fg_color="transparent")
        self._time_label.grid(row=1, column=0)

        self._progress = ctk.CTkProgressBar(card, height=1, fg_color="#0a1a0a",
                                            progress_color=GREEN_DIM, corner_radius=0)
        self._progress.set(1.0)
        self._progress.grid(row=2, column=0, sticky="ew", padx=12, pady=(2, 6))

        self._cycle_lbl = ctk.CTkLabel(card, text="cycle: 00",
                                       font=(MONO, 9), text_color=GREEN_DIM)
        self._cycle_lbl.grid(row=3, column=0, pady=(0, 4))

        ctrl = ctk.CTkFrame(card, fg_color="transparent")
        ctrl.grid(row=4, column=0, sticky="ew", padx=12, pady=(0, 10))
        ctrl.columnconfigure((0, 1), weight=1)

        self._start_btn = ctk.CTkButton(ctrl, text="[ START ]",
                                        font=(MONO, 10, "bold"),
                                        fg_color="#0a1a0a", hover_color="#0f2a0f",
                                        text_color=GREEN, border_width=1,
                                        border_color=GREEN_DIM, corner_radius=3,
                                        height=28, command=self._toggle_timer)
        self._start_btn.grid(row=0, column=0, padx=(0, 3), sticky="ew")

        ctk.CTkButton(ctrl, text="[ ↺ ]", font=(MONO, 11),
                      fg_color="#0a1a0a", hover_color="#0f2a0f",
                      text_color=GREEN_DIM, border_width=1, border_color=GREEN_DIM,
                      corner_radius=3, height=28,
                      command=self._reset_timer).grid(row=0, column=1, padx=(3, 0), sticky="ew")

    # ── Card 2: Quotes ────────────────────────────────────
    def _build_quotes(self, card):
        card.rowconfigure(0, weight=0)  # header
        card.rowconfigure(1, weight=0)  # prefix line
        card.rowconfigure(2, weight=1)  # quote text — expande
        card.rowconfigure(3, weight=0)  # source
        card.rowconfigure(4, weight=0)  # footer hint
        card.columnconfigure(0, weight=1)

        # Header
        ctk.CTkLabel(card, text="// thought.stream",
                     font=(MONO, 9), text_color=GREEN_DIM,
                     anchor="w").grid(row=0, column=0, sticky="ew",
                                     padx=14, pady=(12, 0))


        prefix_row = ctk.CTkFrame(card, fg_color="transparent")
        prefix_row.grid(row=1, column=0, sticky="ew", padx=14, pady=(10, 4))

        self._cursor_label = ctk.CTkLabel(prefix_row, text="█",
                                          font=(MONO, 11), text_color=GREEN)
        self._cursor_label.pack(side="left", padx=(0, 4))

        ctk.CTkLabel(prefix_row, text="thought://",
                     font=(MONO, 10), text_color=GREEN_DIM).pack(side="left")


        self._quote_label = ctk.CTkLabel(
            card, text=self._quote,
            font=(MONO, 13), text_color=TEXT_WHITE,
            wraplength=240, justify="left",
            fg_color="transparent", anchor="nw")
        self._quote_label.grid(row=2, column=0, padx=18, pady=(0, 10), sticky="nsew")

        # Separator line
        ctk.CTkFrame(card, fg_color=BORDER, height=1,
                     corner_radius=0).grid(row=3, column=0, sticky="ew",
                                           padx=14, pady=(0, 6))

        # Source + hint
        bottom = ctk.CTkFrame(card, fg_color="transparent")
        bottom.grid(row=4, column=0, sticky="ew", padx=14, pady=(0, 12))
        bottom.columnconfigure(0, weight=1)

        self._source_label = ctk.CTkLabel(bottom, text=f"— {self._source}",
                                          font=(MONO, 9), text_color=GREEN_DIM,
                                          anchor="w", wraplength=220, justify="left")
        self._source_label.grid(row=0, column=0, sticky="w")

        ctk.CTkLabel(bottom, text="↻ cycle",
                     font=(MONO, 8), text_color=TEXT_DIM,
                     anchor="e").grid(row=0, column=1, sticky="e")

 
    def _build_log_and_heat(self, card):
        self._log_card = card
        card.rowconfigure(0, weight=0)
        card.rowconfigure(1, weight=0)
        card.rowconfigure(2, weight=1)
        card.rowconfigure(3, weight=0)
        card.rowconfigure(4, weight=0)
        card.rowconfigure(5, weight=0)
        card.columnconfigure(0, weight=1)


        hdr = ctk.CTkFrame(card, fg_color="transparent")
        hdr.grid(row=0, column=0, sticky="ew", padx=12, pady=(10, 4))
        hdr.columnconfigure(0, weight=1)
        ctk.CTkLabel(hdr, text="// daily.log",
                     font=(MONO, 9), text_color=GREEN_DIM,
                     anchor="w").grid(row=0, column=0, sticky="w")
        self._log_count_lbl = ctk.CTkLabel(hdr, text=f"[{len(self._log_entries)} entries]",
                                            font=(MONO, 8), text_color=TEXT_DIM, anchor="e")
        self._log_count_lbl.grid(row=0, column=1, sticky="e")


        self._input_frame = ctk.CTkFrame(card, fg_color="#0a140a", corner_radius=4,
                                         border_width=1, border_color=GREEN_DIM)
        ctk.CTkLabel(self._input_frame, text="> task completed:",
                     font=(MONO, 9), text_color=GREEN).pack(anchor="w", padx=8, pady=(6, 2))
        er = ctk.CTkFrame(self._input_frame, fg_color="transparent")
        er.pack(fill="x", padx=8, pady=(0, 6))
        er.columnconfigure(0, weight=1)
        self._task_entry = ctk.CTkEntry(er, font=(MONO, 11), fg_color=BG_ENTRY,
                                        text_color=GREEN, border_color=GREEN_DIM,
                                        border_width=1, corner_radius=3, height=28,
                                        placeholder_text="describe what you accomplished...",
                                        placeholder_text_color=TEXT_DIM)
        self._task_entry.grid(row=0, column=0, sticky="ew", padx=(0, 4))
        self._task_entry.bind("<Return>", lambda e: self._save_task())
        ctk.CTkButton(er, text="[+]", width=36, height=28,
                      fg_color="#0a1a0a", hover_color="#0f280f",
                      text_color=GREEN, font=(MONO, 10, "bold"),
                      border_width=1, border_color=GREEN_DIM, corner_radius=3,
                      command=self._save_task).grid(row=0, column=1, sticky="e")


        self._log_scroll = ctk.CTkScrollableFrame(card, fg_color="transparent",
                                                   scrollbar_button_color=GREEN_DIM,
                                                   scrollbar_button_hover_color=GREEN_MID)
        self._log_scroll.grid(row=2, column=0, sticky="nsew", padx=6, pady=2)
        self._log_scroll.columnconfigure(0, weight=1)

        # Separator
        ctk.CTkFrame(card, fg_color=BORDER, height=1,
                     corner_radius=0).grid(row=3, column=0, sticky="ew", padx=12, pady=(4, 0))

        # ── Heatmap section ───────────────────────────────
        heat_outer = ctk.CTkFrame(card, fg_color="transparent")
        heat_outer.grid(row=4, column=0, sticky="ew", padx=12, pady=(8, 4))
        heat_outer.columnconfigure(0, weight=1)

        # Header do heatmap
        heat_hdr = ctk.CTkFrame(heat_outer, fg_color="transparent")
        heat_hdr.pack(fill="x", pady=(0, 6))
        ctk.CTkLabel(heat_hdr, text="// focus.intensity",
                     font=(MONO, 8), text_color=GREEN_DIM,
                     anchor="w").pack(side="left")
        self._heat_total_lbl = ctk.CTkLabel(heat_hdr, text="",
                                             font=(MONO, 8), text_color=TEXT_DIM,
                                             anchor="e")
        self._heat_total_lbl.pack(side="right")

        # Month labels acima do grid
        self._month_canvas = tk.Canvas(heat_outer, bg=BG_CARD,
                                       highlightthickness=0, height=14)
        self._month_canvas.pack(fill="x")

        # Grid canvas — mais alto para acomodar 7 linhas (dias da semana)
        self._heat_canvas = tk.Canvas(heat_outer, bg=BG_CARD,
                                      highlightthickness=0, height=100)
        self._heat_canvas.pack(fill="x", pady=(1, 0))
        self._heat_canvas.bind("<Configure>", self._draw_heatmap)
        self._heat_canvas.bind("<Motion>", self._heat_hover)
        self._heat_canvas.bind("<Leave>", self._heat_leave)

        # Legenda
        leg = ctk.CTkFrame(heat_outer, fg_color="transparent")
        leg.pack(fill="x", pady=(4, 0))
        ctk.CTkLabel(leg, text="less", font=(MONO, 7), text_color=TEXT_DIM).pack(side="left")
        for col in [HEAT_EMPTY, HEAT_L1, HEAT_L2, HEAT_L3, HEAT_L4, HEAT_MAX]:
            f = tk.Frame(leg, bg=col, width=10, height=10)
            f.pack(side="left", padx=1)
        ctk.CTkLabel(leg, text="more", font=(MONO, 7),
                     text_color=TEXT_DIM).pack(side="left", padx=(2, 0))

        # Footer
        ctk.CTkLabel(card, text="saved to: zenith_log.json",
                     font=(MONO, 7), text_color=TEXT_DIM,
                     anchor="e").grid(row=5, column=0, sticky="e", padx=12, pady=(2, 8))

        self._render_log()
        self.after(200, self._draw_heatmap)


    def _draw_heatmap(self, event=None):
        canvas = self._heat_canvas
        month_canvas = self._month_canvas
        canvas.delete("all")
        month_canvas.delete("all")
        self._heat_cells = {}

        counts = entries_per_day(self._log_entries)
        total  = sum(counts.values())
        self._heat_total_lbl.configure(
            text=f"{total} sessions / 30d" if total else "no sessions yet")

        W = canvas.winfo_width()
        if W < 10:
            return

        DAYS   = 30          
        CELL   = 12          
        GAP    = 3           
        STEP   = CELL + GAP
        ROWS   = 7           
        LEFT   = 24          
 
        today     = date.today()
        today_wd  = today.weekday()          # 0=seg ... 6=dom

        today_wd_sun = (today_wd + 1) % 7


        max_cols = max(5, (W - LEFT - 4) // STEP)

        total_slots = max_cols * ROWS

        slot_today = total_slots - 1

        days_before_today = slot_today - today_wd_sun - (max_cols - 1) * ROWS
 
        slot_of_today = (max_cols - 1) * ROWS + today_wd_sun

        TOP = 2

        prev_month = None
        for slot in range(slot_of_today - DAYS + 1, slot_of_today + 1):
            col  = slot // ROWS
            row  = slot % ROWS
            days_ago = slot_of_today - slot
            d    = today - timedelta(days=days_ago)
            key  = day_key(d)
            count = counts.get(key, 0)
            color = heat_color(count)

            x0 = LEFT + col * STEP
            y0 = TOP  + row * STEP
            x1 = x0 + CELL
            y1 = y0 + CELL


            if d == today:
                rect_id = canvas.create_rectangle(
                    x0, y0, x1, y1, fill=color, outline=GREEN_MID, width=1)
            else:
                rect_id = canvas.create_rectangle(
                    x0, y0, x1, y1, fill=color, outline="#222222", width=1)

            self._heat_cells[rect_id] = (key, count, d)

            # Label de mês no month_canvas (aparece na primeira semana do mês)
            if d.day <= 7 and d.month != prev_month:
                prev_month = d.month
                mx = LEFT + col * STEP
                month_canvas.create_text(mx, 7, text=d.strftime("%b"),
                                         fill=GREEN_DIM,
                                         font=("Consolas", 7), anchor="w")


        day_names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for row in [0, 2, 4, 6]:
            y = TOP + row * STEP + CELL // 2
            canvas.create_text(LEFT - 3, y, text=day_names[row],
                               fill=TEXT_DIM, font=("Consolas", 7), anchor="e")

        # Altura dinâmica
        canvas.configure(height=TOP + ROWS * STEP + 2)

    def _heat_hover(self, event):
        items = self._heat_canvas.find_overlapping(event.x, event.y, event.x, event.y)
        for item in items:
            if item in self._heat_cells:
                key, count, d = self._heat_cells[item]
                label = f"  {d.strftime('%a')} {key}  →  {count} task{'s' if count != 1 else ''}  "
                self._show_tooltip(event, label)
                return
        self._hide_tooltip()

    def _heat_leave(self, event):
        self._hide_tooltip()

    def _show_tooltip(self, event, text):
        self._hide_tooltip()
        x = self._heat_canvas.winfo_rootx() + event.x + 14
        y = self._heat_canvas.winfo_rooty() + event.y - 26
        self._tooltip_win = tk.Toplevel(self)
        self._tooltip_win.wm_overrideredirect(True)
        self._tooltip_win.wm_geometry(f"+{x}+{y}")
        tk.Label(self._tooltip_win, text=text,
                 font=("Consolas", 9), fg=GREEN, bg="#0c1a0c",
                 padx=6, pady=3, relief="flat",
                 highlightthickness=1, highlightbackground=GREEN_DIM).pack()

    def _hide_tooltip(self):
        if self._tooltip_win:
            try:
                self._tooltip_win.destroy()
            except Exception:
                pass
            self._tooltip_win = None

    # ── Log ───────────────────────────────────────────────
    def _render_log(self):
        for w in self._log_scroll.winfo_children():
            w.destroy()
        if not self._log_entries:
            ctk.CTkLabel(self._log_scroll,
                         text="no entries yet.\ncomplete a pomodoro to log a task.",
                         font=(MONO, 9), text_color=TEXT_DIM,
                         justify="left", anchor="nw").pack(anchor="nw", padx=4, pady=8)
            return
        for entry in reversed(self._log_entries):
            row = ctk.CTkFrame(self._log_scroll, fg_color="transparent")
            row.pack(fill="x", pady=1)
            row.columnconfigure(1, weight=1)
            ctk.CTkLabel(row, text=entry["time"],
                         font=(MONO, 8), text_color=GREEN_DIM,
                         width=90, anchor="w").grid(row=0, column=0, sticky="w")
            ctk.CTkLabel(row, text=f"| {entry['task']}",
                         font=(MONO, 10), text_color=TEXT_WHITE,
                         anchor="w", wraplength=320,
                         justify="left").grid(row=0, column=1, sticky="ew", padx=(4, 0))
        self._log_count_lbl.configure(text=f"[{len(self._log_entries)} entries]")

    def _show_log_input(self):
        self._awaiting_log = True
        self._input_frame.grid(row=1, column=0, sticky="ew", padx=12, pady=(0, 4))
        self._task_entry.delete(0, "end")
        self._task_entry.focus_set()

    def _save_task(self):
        task = self._task_entry.get().strip()
        if not task:
            return
        self._log_entries.append({"time": now_stamp(), "task": task})
        save_log(self._log_entries)
        self._task_entry.delete(0, "end")
        self._input_frame.grid_remove()
        self._awaiting_log = False
        self._render_log()
        self._draw_heatmap()

    # ── Timer ─────────────────────────────────────────────
    def _tick(self):
        if self.timer_running and self.pomodoro_seconds > 0:
            self.pomodoro_seconds -= 1
            self._time_label.configure(text=fmt_time(self.pomodoro_seconds))
            self._progress.set(self.pomodoro_seconds / (POMODORO_MINUTES * 60))
            if self.pomodoro_seconds == 0:
                self._on_pomodoro_end()
        self.after(1000, self._tick)

    def _toggle_timer(self):
        self.timer_running = not self.timer_running
        self._start_btn.configure(text="[ PAUSE ]" if self.timer_running else "[ START ]")

    def _reset_timer(self):
        self.timer_running = False
        self.pomodoro_seconds = POMODORO_MINUTES * 60
        self._start_btn.configure(text="[ START ]")
        self._time_label.configure(text=fmt_time(self.pomodoro_seconds), text_color=GREEN)
        self._progress.set(1.0)
        self._pcard_ref.configure(fg_color=BG_CARD)
        if self._awaiting_log:
            self._input_frame.grid_remove()
            self._awaiting_log = False

    def _on_pomodoro_end(self):
        self.timer_running = False
        self._start_btn.configure(text="[ START ]")
        self._time_label.configure(text="00:00", text_color=AMBER)
        self._pcard_ref.configure(fg_color=BG_CARD_END)
        self.cycle_count += 1
        self._cycle_lbl.configure(text=f"cycle: {self.cycle_count:02d}")
        self._bar_cycle.configure(text=f"[cycles: {self.cycle_count:02d}]")
        self._quote, self._source = random.choice(QUOTES)
        self._quote_label.configure(text=self._quote)
        self._source_label.configure(text=f"— {self._source}")
        self._show_log_input()

    def _blink_cursor(self):
        self._cursor_visible = not self._cursor_visible
        self._cursor_label.configure(text_color=GREEN if self._cursor_visible else BG_CARD)
        self.after(530, self._blink_cursor)

    def _bind_drag(self):
        self._bar.bind("<ButtonPress-1>", self._drag_start)
        self._bar.bind("<B1-Motion>", self._drag_move)
        for child in self._bar.winfo_children():
            child.bind("<ButtonPress-1>", self._drag_start)
            child.bind("<B1-Motion>", self._drag_move)

    def _drag_start(self, e):
        self._drag_x = e.x_root - self.winfo_x()
        self._drag_y = e.y_root - self.winfo_y()

    def _drag_move(self, e):
        self.geometry(f"+{e.x_root - self._drag_x}+{e.y_root - self._drag_y}")

    def _resize_start(self, e):
        self._resize_x = e.x_root
        self._resize_y = e.y_root
        self._resize_w = self.winfo_width()
        self._resize_h = self.winfo_height()

    def _resize_move(self, e):
        nw = max(820, self._resize_w + (e.x_root - self._resize_x))
        nh = max(480, self._resize_h + (e.y_root - self._resize_y))
        self.geometry(f"{nw}x{nh}")

    def _toggle_pin(self):
        self._pinned = not self._pinned
        self.attributes("-topmost", self._pinned)
        self._pin_btn.configure(text_color=GREEN if self._pinned else TEXT_DIM)


if __name__ == "__main__":
    app = ZenithApp()
    app.mainloop()