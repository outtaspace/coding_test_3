package CityInfo::Command;

use v5.22;
use strict;
use warnings;
use JIP::ClassField;
use Carp qw(confess);
use English qw(-no_match_vars);

has [qw(reader writer)] => (get => q{+}, set => q{+});

my $regex = qr{
    ^
    (\d+)
    \.
    \s+
    ([^;,]+)[;,.]?
    \s+
    ([^;,]+)[;,.]?
    \s-\s
    (.+)
    $
}x;

sub new {
    my ($class, %param) = @ARG;

    return bless({}, $class)
        ->set_reader($param{reader})
        ->set_writer($param{writer});
}

sub execute {
    confess 'execute() has no implementation in the abstract class';
}

sub parse_line {
    my ($self, $line) = @ARG;

    my ($id, $city, $country, $population) = $line =~ $regex;

    return {
        id         => $id,
        city       => $city,
        country    => $country,
        population => $population,
    };
}

1;

