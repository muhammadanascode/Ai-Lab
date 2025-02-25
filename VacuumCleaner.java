import java.util.Random;

public class VacuumCleaner {

  String current_location = "";
  int points = 0;
  Random rn = new Random();

  void clean(String[][] squares, String start_location) {
    this.current_location = start_location;
    int moves = 5; // Run for 5 moves

    while (moves > 0) {
      // Find current square index
      int index = this.current_location.equals("A") ? 0 : 1;

      // Cleaning logic
      if (squares[index][1].equals("Dirt")) {
        System.out.println("Cleaning " + squares[index][0]);
        squares[index][1] = "Clean";
        points++;
      } else {
        System.out.println(squares[index][0] + " is already clean.");
      }

      // Move to the other square
      if (this.current_location.equals("A")) {
        move_right();
      } else {
        move_left();
      }

      if (rn.nextInt(100) < 50) { //50% chance of dirt
        squares[index][1] = "Dirt";
      }

      moves--;
    }
  }

  void move_right() {
    this.current_location = "B";
    System.out.println("Moving Right ----->> " + this.current_location);
  }

  void move_left() {
    this.current_location = "A";
    System.out.println("Moving Left ----->> " + this.current_location);
  }

  int getPoints() {
    return this.points;
  }

  public static void main(String[] args) {
    String[][] squares = { { "A", "Dirt" }, { "B", "Dirt" } };
    VacuumCleaner vc = new VacuumCleaner();
    vc.clean(squares, "A");

    System.out.println("Total points earned: " + vc.getPoints());
  }
}
