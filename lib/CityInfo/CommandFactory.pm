package CityInfo::CommandFactory;

use v5.22;
use strict;
use warnings;
use English qw(-no_match_vars);

sub create {
    my ($class, %param) = @ARG;

    my $mode = ucfirst $param{mode};

    my $command_location = sprintf 'CityInfo/Command/%s.pm', $mode;
    my $command_class    = sprintf 'CityInfo::Command::%s',  $mode;

    require $command_location;

    return $command_class->new(%{ $param{xargs} });
}

1;

