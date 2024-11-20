use eframe::{egui, App, CreationContext};
use rand::Rng;

struct GameState {
    user_choice: String,
    computer_choice: String,
    result: String,
    is_playing: bool,
}

impl GameState {
    fn new() -> Self {
        GameState {
            user_choice: String::new(),
            computer_choice: String::new(),
            result: String::new(),
            is_playing: true,
        }
    }

    fn play_round(&mut self, user_choice: String) {
        let choices = ["rock", "paper", "scissors"];
        let mut rng = rand::thread_rng();

        self.user_choice = user_choice;
        self.computer_choice = choices[rng.gen_range(0..3)].to_string();

        // Ergebnisberechnung
        self.result = match (self.user_choice.as_str(), self.computer_choice.as_str()) {
            ("rock", "scissors") | ("scissors", "paper") | ("paper", "rock") => "You win!".to_string(),
            ("scissors", "rock") | ("paper", "scissors") | ("rock", "paper") => "You lose!".to_string(),
            _ => "It's a tie!".to_string(),
        };
    }
}

impl App for GameState {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            if self.is_playing {
                ui.horizontal(|ui| {
                    if ui.button("Rock").clicked() {
                        self.play_round("rock".to_string());
                    }
                    if ui.button("Paper").clicked() {
                        self.play_round("paper".to_string());
                    }
                    if ui.button("Scissors").clicked() {
                        self.play_round("scissors".to_string());
                    }
                });

                ui.separator();
                ui.label(format!("You chose: {}", self.user_choice));
                ui.label(format!("Computer chose: {}", self.computer_choice));
                ui.label(format!("Result: {}", self.result));

                if ui.button("Stop").clicked() {
                    self.is_playing = false;
                    ui.label("Game Stopped!");
                }
            } else {
                ui.label("Game Over! Press 'Stop' to restart.");
            }
        });
    }
}

fn main() {
    let app = |cc: &CreationContext| {
        Box::new(GameState::new()) as Box<dyn App>
    };

    eframe::run_native(
        "Rock, Paper, Scissors",
        eframe::NativeOptions {
            initial_window_size: Some(egui::vec2(400.0, 300.0)),
            ..Default::default()
        },
        Box::new(app),
    );
}
