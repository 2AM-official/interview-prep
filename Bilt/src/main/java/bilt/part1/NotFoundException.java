package bilt.part1;

public class NotFoundException extends RuntimeException {
    public NotFoundException() {
        super("user not found");
    }
}
