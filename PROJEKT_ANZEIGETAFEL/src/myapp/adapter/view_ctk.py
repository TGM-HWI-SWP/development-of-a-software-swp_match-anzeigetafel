import customtkinter as ctk


class CTkView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        # Fenster
        self.title("⚽ Match-Anzeigetafel")
        self.geometry("700x500")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        # ----------------------
        # Teamnamen
        # ----------------------
        self.team_frame = ctk.CTkFrame(self)
        self.team_frame.pack(pady=15, fill="x", padx=20)

        self.home_entry = ctk.CTkEntry(self.team_frame, placeholder_text="Heimmannschaft")
        self.home_entry.pack(side="left", padx=10, expand=True, fill="x")

        self.away_entry = ctk.CTkEntry(self.team_frame, placeholder_text="Auswärtsmannschaft")
        self.away_entry.pack(side="left", padx=10, expand=True, fill="x")

        self.btn_set_teams = ctk.CTkButton(
            self.team_frame, text="✔ Teams setzen", command=self.set_teams
        )
        self.btn_set_teams.pack(side="left", padx=10)

        # ----------------------
        # Anzeige Teamnamen
        # ----------------------
        self.name_label = ctk.CTkLabel(self, text="Heim  vs  Gast", font=("Arial Black", 22))
        self.name_label.pack(pady=10)

        # ----------------------
        # Scoreboard
        # ----------------------
        self.score_label = ctk.CTkLabel(self, text="0 : 0", font=("Arial Black", 42), text_color="lime")
        self.score_label.pack(pady=10)

        self.goal_frame = ctk.CTkFrame(self)
        self.goal_frame.pack(pady=5)

        ctk.CTkButton(self.goal_frame, text="⚽ Tor Heim", command=self.controller.goal_home).pack(side="left", padx=10)
        ctk.CTkButton(self.goal_frame, text="⚽ Tor Gast", command=self.controller.goal_away).pack(side="left", padx=10)

        # ----------------------
        # Timer
        # ----------------------
        self.timer_label = ctk.CTkLabel(self, text="00:00", font=("Arial Black", 30))
        self.timer_label.pack(pady=15)

        self.timer_buttons = ctk.CTkFrame(self)
        self.timer_buttons.pack()

        ctk.CTkButton(self.timer_buttons, text="▶ Start", command=self.controller.start_timer).pack(side="left", padx=5)
        ctk.CTkButton(self.timer_buttons, text="⏸ Pause", command=self.controller.pause_timer).pack(side="left", padx=5)
        ctk.CTkButton(self.timer_buttons, text="⏹ Reset", command=self.controller.reset_timer).pack(side="left", padx=5)

    # =========================
    # Methoden für Controller
    # =========================
    def set_teams(self):
        home = self.home_entry.get()
        away = self.away_entry.get()
        if home and away:
            self.name_label.configure(text=f"{home}  vs  {away}")

    def update_score(self, home, away):
        self.score_label.configure(text=f"{home} : {away}")

    def update_timer(self, minutes, seconds):
        self.timer_label.configure(text=f"{minutes:02}:{seconds:02}")

    def show_teams(self, teams):
    # Alte Labels löschen
        if hasattr(self, 'team_labels'):
            for lbl in self.team_labels:
                lbl.destroy()
        else:
            self.team_labels = []

    # Neue Labels erstellen
        for team in teams:
            lbl = ctk.CTkLabel(self, text=team.name, font=("Arial", 16))
            lbl.pack()
        self.team_labels.append(lbl)

