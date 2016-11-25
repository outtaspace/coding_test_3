package CityInfo::Command::All;

use parent qw(CityInfo::Command);

use v5.22;
use strict;
use warnings;
use Data::Dumper;
use Carp qw(confess);
use English qw(-no_match_vars);

sub execute {
    my $self = shift;

    my $all_lines = do {
        local $INPUT_RECORD_SEPARATOR = undef;
        $self->reader->getline;
    };

    my $descriptions = [];
    while ($all_lines =~ m{([^\n]+)\n?}xg) {
        my $description = $self->parse_line($1);
        push @{ $descriptions }, $description if defined $description->{id};
    }

    $self->write_summary($descriptions);
}

sub write_summary {
    my ($self, $descriptions) = @ARG;

    $self->writer->say(Dumper $descriptions);
}

1;

