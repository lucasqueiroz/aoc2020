#!/usr/bin/perl
open(my $in, "<", "day-3/input");
my @lines = <$in>;

my $repeats = ($#lines + 1) * 3;

my $i = 0;
my $trees = 0;

foreach my $line (@lines) {
    $line =~ s/\R//g;
    $line = "$line" x $repeats;
    my $char = substr($line, $i, 1);
    if ( "$char" eq "#" ) {
        $trees = $trees + 1;
    }
    $i = $i + 3;
}

print("$trees\n");

