import customtkinter as ctk

class CTkView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        # Fenster
        self.title("⚽ Match-Anzeigetafel")
        self.geometry("700x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        # Teams Eingabe
        self.team_frame = ctk.CTkFrame(self)
        self.team_frame.pack(pady=10, fill="x", padx=20)

        self.home_entry = ctk.CTkEntry(self.team_frame, placeholder_text="Heimmannschaft")
        self.home_entry.pack(side="left", padx=10, expand=True, fill="x")

        self.away_entry = ctk.CTkEntry(self.team_frame, placeholder_text="Auswärtsmannschaft")
        self.away_entry.pack(side="left", padx=10, expand=True, fill="x")

        self.btn_set_teams = ctk.CTkButton(
            self.team_frame, text="✔ Teams setzen", command=self.set_teams
        )
        self.btn_set_teams.pack(side="left", padx=10)

        # Anzeige Teamnamen
        self.name_label = ctk.CTkLabel(self, text="Heim  vs  Gast", font=("Arial Black", 22))
        self.name_label.pack(pady=10)

        # Scoreboard
        self.score_label = ctk.CTkLabel(self, text="0 : 0", font=("Arial Black", 42), text_color="lime")
        self.score_label.pack(pady=10)

        self.goal_frame = ctk.CTkFrame(self)
        self.goal_frame.pack(pady=5)

        ctk.CTkButton(self.goal_frame, text="⚽ Tor Heim", command=self.controller.goal_home).pack(side="left", padx=10)
        ctk.CTkButton(self.goal_frame, text="⚽ Tor Gast", command=self.controller.goal_away).pack(side="left", padx=10)

        # Timer
        self.timer_label = ctk.CTkLabel(self, text="00:00", font=("Arial Black", 30))
        self.timer_label.pack(pady=15)

        self.timer_buttons = ctk.CTkFrame(self)
        self.timer_buttons.pack()

        ctk.CTkButton(self.timer_buttons, text="▶ Start", command=self.controller.start_timer).pack(side="left", padx=5)
        ctk.CTkButton(self.timer_buttons, text="⏸ Pause", command=self.controller.pause_timer).pack(side="left", padx=5)
        ctk.CTkButton(self.timer_buttons, text="⏹ Reset", command=self.controller.reset_timer).pack(side="left", padx=5)

        # Spieleranzeige
        self.player_frame = ctk.CTkFrame(self)
        self.player_frame.pack(pady=10, fill="both", expand=True)
        self.player_labels = []

        # Aktuelles Match unten
        self.current_match_label = ctk.CTkLabel(self, text="Heim vs Gast", font=("Arial Black", 20))
        self.current_match_label.pack(pady=10)

        # interne Listen für Labels
        self.team_labels = []

    # ----------------------
    # Teams setzen
    # ----------------------
    def set_teams(self):
        home = self.home_entry.get()
        away = self.away_entry.get()
        if home and away:
            # Großes Label
            self.name_label.configure(text=f"{home}  vs  {away}")
            # Unten
            self.current_match_label.configure(text=f"{home}  vs  {away}")

    # ----------------------
    # Scoreboard aktualisieren
    # ----------------------
    def update_score(self, home, away):
        self.score_label.configure(text=f"{home} : {away}")

    # ----------------------
    # Score blinkt bei Tor
    # ----------------------
    def blink_score(self, times=6, interval=200):
        def _blink(count):
            if count > 0:
                current_color = self.score_label.cget("text_color")
                new_color = "red" if current_color != "red" else "lime"
                self.score_label.configure(text_color=new_color)
                self.after(interval, _blink, count - 1)
            else:
                self.score_label.configure(text_color="lime")
        _blink(times)

    # ----------------------
    # Timer aktualisieren
    # ----------------------
    def update_timer(self, minutes, seconds):
        self.timer_label.configure(text=f"{minutes:02}:{seconds:02}")

    # ----------------------
    # Teams anzeigen
    # ----------------------
    def show_teams(self, teams):
        for lbl in self.team_labels:
            lbl.destroy()
        self.team_labels = []

        for team in teams:
            lbl = ctk.CTkLabel(self, text=team.name, font=("Arial", 16))
            lbl.pack()
            self.team_labels.append(lbl)

        # optional: erstes zwei Teams im Match-Label
        if len(teams) >= 2:
            self.name_label.configure(text=f"{teams[0].name}  vs  {teams[1].name}")
            self.current_match_label.configure(text=f"{teams[0].name}  vs  {teams[1].name}")

    # ----------------------
    # Spieler anzeigen
    # ----------------------
    def show_players(self, players):
        for lbl in self.player_labels:
            lbl.destroy()
        self.player_labels = []

        for p in players:
            lbl = ctk.CTkLabel(self.player_frame, text=f"{p.name} #{p.nummer} ⚽ {p.tore}", font=("Arial", 14))
            lbl.pack(pady=2, anchor="w")
            self.player_labels.append(lbl)


