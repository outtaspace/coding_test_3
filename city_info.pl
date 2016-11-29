#!/usr/bin/perl

use v5.22;
use strict;
use warnings;
use lib::abs qw(lib);
use IO::File;
use IO::Handle;
use Carp qw(croak);
use Pod::Usage qw(pod2usage);
use Getopt::Long qw(GetOptions);
use English qw(-no_match_vars);
use CityInfo::CommandFactory;

use constant FILENAME => lib::abs::path('./city_info.txt');

#-- CLI ----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
my $options = {};
GetOptions($options, 'help', 'all', 'city=s', 'filename=s')
    or croak 'Error in command line arguments';

if (!%{ $options } || exists $options->{help}) {
    pod2usage(-verbose => 2, -exitval => 0);
}

#-- open a data file ---------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
my $filehandle;
{
    my $filename = exists $options->{filename} ? $options->{filename} : FILENAME;

    $filehandle = IO::File->new($filename, 'r');

    croak(sprintf q{Can't open "%s": %s}, $filename, $OS_ERROR)
        unless $filehandle;
}

#-- instantiate a command ----------------------------------------------------------------
#-----------------------------------------------------------------------------------------
my $command = do {
    my ($mode, %xargs);

    if (exists $options->{city}) {
        $mode = 'city';

        $xargs{city} = $options->{city};
    }
    elsif (exists $options->{all}) {
        $mode = 'all';
    }

    my $input_filehandle = IO::Handle->new;
    if ($input_filehandle->fdopen($filehandle, 'r')) {
        $xargs{reader} = $input_filehandle;
    }
    else {
        croak q{Can't open input file: }. $OS_ERROR;
    }

    my $output_filehandle = IO::Handle->new;
    if ($output_filehandle->fdopen(fileno(STDOUT), 'w')) {
        $xargs{writer} = $output_filehandle;
    }
    else {
        croak q{Can't open STDOUT: }. $OS_ERROR;
    }

    CityInfo::CommandFactory->create(mode => $mode, xargs => \%xargs);
};

#-- do command ---------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
$command->execute();

#-- end ----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

__END__


=head1 NAME

city_info.pl

=head1 SYNOPSIS

city_info.pl [options]

Options:

    --help            brief help message
    --all             provide summary information for all cities
    --filename        optional filename holding the city info

=head1 DESCRIPTION

This program will print out a summary of the details of the city
including ID, City, Country, and Population.

If the --all option is also specified then this program collects and provides
summary information for all cities.

=cut

