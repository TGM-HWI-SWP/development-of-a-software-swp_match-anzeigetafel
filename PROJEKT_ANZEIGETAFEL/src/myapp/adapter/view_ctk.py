import customtkinter as ctk


class CTkView(ctk.CTk):

    def _init_(self):
        super()._init_()

        self.title("Stadionanzeigetafel")
        self.geometry("800x500")

        # Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        # --- Left: Teams ---
        team_frame = ctk.CTkFrame(self)
        team_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        team_label = ctk.CTkLabel(team_frame, text="Teams", font=("Arial", 20))
        team_label.pack(pady=5)

        team_listbox = ctk.CTkScrollableFrame(team_frame, width=200)
        team_listbox.pack(fill="both", expand=True)

        # --- Center: Players ---
        player_frame = ctk.CTkFrame(self)
        player_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        player_label = ctk.CTkLabel(player_frame, text="Spieler", font=("Arial", 20))
        player_label.pack(pady=5)

        player_listbox = ctk.CTkScrollableFrame(player_frame)
        player_listbox.pack(fill="both", expand=True)

        # --- Bottom: Scoreboard ---
        score_frame = ctk.CTkFrame(self)
        score_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

        score_label = ctk.CTkLabel(score_frame, text="0 : 0", font=("Arial", 32))
        score_label.pack(pady=5)

        btn_home = ctk.CTkButton(score_frame, text="Tor Heim")
        btn_home.pack(side="left", padx=10)

        btn_away = ctk.CTkButton(score_frame, text="Tor Auswärts")
        btn_away.pack(side="left", padx=10)
