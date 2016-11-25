package CityInfo::Command::City;

use parent qw(CityInfo::Command);

use v5.22;
use strict;
use warnings;
use JIP::ClassField;
use Carp qw(confess);
use English qw(-no_match_vars);

has city => (get => q{+}, set => q{+});

sub new {
    my ($class, %param) = @ARG;

    my $self = $class->SUPER::new(%param);

    return $self->set_city($param{city});
}

sub execute {
    my $self = shift;

    while (defined(my $each_line = $self->reader->getline)) {
        chomp $each_line;

        my $description = $self->parse_line($each_line);

        if (defined $description->{city} && $description->{city} eq $self->city) {
            $self->write_summary($description);
        }
    }
}

sub write_summary {
    my ($self, $description) = @ARG;

    my $summary = sprintf 'id=%d; city=%s; country=%s; population=%s',
        $description->{id},
        $description->{city},
        $description->{country},
        $description->{population};

    $self->writer->say($summary);
}

1;

