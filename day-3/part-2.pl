#!/usr/bin/perl
open(my $in, "<", "day-3/input");
my @lines = <$in>;

my $repeats = ($#lines + 1) * 3;

my $i = 0;
my $j = 0;
my $k = 0;
my $l = 0;
my $m = 0;
my $ln = 0;
my @trees = (0, 0, 0, 0, 0);

foreach my $line (@lines) {
    $line =~ s/\R//g;
    $line = "$line" x $repeats;

    # Right 1
    my $char = substr($line, $i, 1);
    if ( "$char" eq "#" ) {
        $trees[0] = $trees[0] + 1;
    }
    $i = $i + 1;

    # Right 3
    my $char = substr($line, $j, 1);
    if ( "$char" eq "#" ) {
        $trees[1] = $trees[1] + 1;
    }
    $j = $j + 3;

    # Right 5
    $char = substr($line, $k, 1);
    if ( "$char" eq "#" ) {
        $trees[2] = $trees[2] + 1;
    }
    $k = $k + 5;

    # Right 7
    $char = substr($line, $l, 1);
    if ( "$char" eq "#" ) {
        $trees[3] = $trees[3] + 1;
    }
    $l = $l + 7;

    # Right 1, Down 2
    if ( $ln % 2 == 0 ) {
        $char = substr($line, $m, 1);
        if ( "$char" eq "#" ) {
            $trees[4] = $trees[4] + 1;
        }
        $m = $m + 1;
    }

    $ln = $ln + 1;

}

my $prod = $trees[0] * $trees[1] * $trees[2] * $trees[3] * $trees[4];

print("$prod\n");

