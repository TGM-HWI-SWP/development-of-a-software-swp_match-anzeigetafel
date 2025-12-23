class AnzeigetafelController:
    def __init__(self, db, view=None):
        self.db = db
        self.view = view

        # Score
        self.score_home = 0
        self.score_away = 0

        # Timer
        self.seconds = 0
        self.timer_running = False

    def set_view(self, view):
        self.view = view

    # ======================
    # Score
    # ======================
    def goal_home(self):
        self.score_home += 1
        if self.view:
            self.view.update_score(self.score_home, self.score_away)

    def goal_away(self):
        self.score_away += 1
        if self.view:
            self.view.update_score(self.score_home, self.score_away)

    # ======================
    # Timer
    # ======================
    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self._tick()

    def _tick(self):
        if self.timer_running and self.view:
            self.seconds += 1
            minutes = self.seconds // 60
            seconds = self.seconds % 60
            self.view.update_timer(minutes, seconds)
            self.view.after(1000, self._tick)

    def pause_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.seconds = 0
        if self.view:
            self.view.update_timer(0, 0)

    # ======================
    # Teams
    # ======================
    def show_all_teams(self):
        teams = self.db.get_teams()
        if self.view:
            self.view.show_teams(teams)


    # In AnzeigetafelController.py
    def goal_home(self):
        self.score_home += 1
        if self.view:
            self.view.update_score(self.score_home, self.score_away)
            self.view.blink_score()

    def goal_away(self):
        self.score_away += 1
        if self.view:
            self.view.update_score(self.score_home, self.score_away)
            self.view.blink_score()
