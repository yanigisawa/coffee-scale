#!/usr/bin/env python
from golbase import GameOfLifeBase, Cell
import random
import time
import logging
import json
import requests
import os


class GameOfLifeRandom(GameOfLifeBase):
    def __init__(self, *args, **kwargs):
        super(GameOfLifeRandom, self).__init__(*args, **kwargs)
        self.toroidal = True
        self.generations = 0

    def reset(self):
        self.save_gol_iteration()
        self.initializeCells()
        self._initialState = None
        self._evolutionQueue = []
        self._lights_per_evolution = []
        self.get_random_config()
        self.generations = 0

    def get_random_config(self):
        # self.set_manual_config()
        # return

        self.initializeCells()
        # active_cells = random.randint(10, self.matrix.width * self.matrix.height)
        active_cells = random.randint(10, 200)
        for _ in range(active_cells):
            x = random.randint(0, self.matrix.width -1)
            y = random.randint(0, self.matrix.height - 1)
            self.cells[x][y].alive = True

    def save_gol_iteration(self):
        url = "https://gol-initial-states.anvil.app/_/api/"
        alive_cell_counts = [len(s.split(";")) for s in self._evolutionQueue]
        data = {
            "initial_state": self._initialState,
            "generations": self.generations,
            "likely_gliding": len(set(alive_cell_counts)) == 1,
            "likely_spaceship": len(set(alive_cell_counts)) == 2,
            "light_counts": {
                "lights_per_evolution": self._lights_per_evolution
            }
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": os.environ.get("AUTH_HEADER", "")
        }
        try:
            requests.post(url, headers=headers, data=json.dumps(data), timeout=5)
        except:
            pass


    def set_manual_config(self):
        point_str = "0:20;1:2;1:20;1:24;1:25;2:25;2:26;2:27;3:16;3:18;3:20;3:21;3:23;3:25;4:21;4:28;5:1;5:6;6:6;8:19;8:23;9:17;9:23;9:25;9:28;10:4;10:19;10:20;10:21;10:22;10:25;11:13;11:14;11:15;11:18;11:23;12:7;12:13;12:21;12:23;13:5;13:23;14:6;14:8;14:31;15:17;15:18;16:3;16:4;16:5;16:6;16:30;16:31;17:17;18:1;18:4;18:5;18:17;18:21;18:31;19:1;19:31;20:9;20:20;21:20;22:12;22:13;23:12;23:15;23:20;23:21;24:7;24:8;24:9;24:11;24:12;24:14;24:24;25:7;25:12;25:14;25:15;25:18;25:19;25:21;25:29;26:5;26:6;26:7;26:8;26:9;26:10;26:11;26:12;26:13;27:0;27:12;27:13;27:17;27:18;27:29;27:30;28:4;28:9;28:12;29:2;29:16;30:2;31:1;31:2;31:7;31:8;31:9;31:22;31:26;31:31;32:2;33:2;33:6;33:8;33:16;33:17;33:21;33:27;33:30;34:0;34:16;34:17;34:18;34:19;34:23;34:25;34:27;35:0;35:1;35:2;35:16;35:18;35:25;36:0;36:16;36:18;37:2;37:12;37:16;37:27;38:1;38:2;38:3;38:8;38:14;38:27;38:29;39:0;39:13;39:14;39:15;39:17;40:13;40:15;41:16;41:18;41:23;42:23;42:25;43:3;43:4;43:5;43:7;43:10;43:23;44:4;44:5;44:24;44:25;45:5;45:22;46:3;46:4;46:13;46:24;46:26;46:27;46:30;47:4;47:24;48:2;48:7;48:22;48:23;48:25;48:27;49:24;50:1;50:2;50:23;50:25;50:26;51:1;51:2;51:14;51:18;51:19;52:1;52:9;52:19;52:24;52:26;53:1;53:3;53:16;53:17;53:18;53:19;53:23;53:24;54:0;54:1;54:2;54:25;54:27;55:2;55:3;55:5;56:2;57:3;57:4;57:17;57:19;58:3;58:17;58:19;59:9;59:17;59:19;60:8;60:14;60:15;60:16;60:17;60:18;61:0;61:8;61:12;61:13;61:31;62:0;62:6;62:8;62:14;62:28;62:30;63:20;"
        points = point_str.split(";")
        for p in points:
            if not p:
                continue
            row, col = [int(x) for x in p.split(":")]
            self.cells[row][col].alive = True

    def run(self):
        self.initializeCells()

        self.get_random_config()

        ms_delay = 1 # 0.01
        print("delay = {0}".format(ms_delay))
        while True:

            self.drawCells()
            self.canvas = self.matrix.SwapOnVSync(self.canvas)

            time.sleep(random.randint(1, 5))
            self.get_random_config()
            # self.evolve()
            # self.generations += 1
            # if self.generations % 1000 == 0:
            #     self.save_gol_iteration()



# Main function
if __name__ == "__main__":
    gol = GameOfLifeRandom()
    if (not gol.process()):
        gol.print_help()
