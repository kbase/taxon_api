package TaxonAPI::TaxonAPIClient;

use JSON::RPC::Client;
use POSIX;
use strict;
use Data::Dumper;
use URI;
use Bio::KBase::Exceptions;
my $get_time = sub { time, 0 };
eval {
    require Time::HiRes;
    $get_time = sub { Time::HiRes::gettimeofday() };
};

use Bio::KBase::AuthToken;

# Client version should match Impl version
# This is a Semantic Version number,
# http://semver.org
our $VERSION = "0.1.0";

=head1 NAME

TaxonAPI::TaxonAPIClient

=head1 DESCRIPTION


A KBase module: TaxonAPI


=cut

sub new
{
    my($class, $url, @args) = @_;
    

    my $self = {
	client => TaxonAPI::TaxonAPIClient::RpcClient->new,
	url => $url,
	headers => [],
    };

    chomp($self->{hostname} = `hostname`);
    $self->{hostname} ||= 'unknown-host';

    #
    # Set up for propagating KBRPC_TAG and KBRPC_METADATA environment variables through
    # to invoked services. If these values are not set, we create a new tag
    # and a metadata field with basic information about the invoking script.
    #
    if ($ENV{KBRPC_TAG})
    {
	$self->{kbrpc_tag} = $ENV{KBRPC_TAG};
    }
    else
    {
	my ($t, $us) = &$get_time();
	$us = sprintf("%06d", $us);
	my $ts = strftime("%Y-%m-%dT%H:%M:%S.${us}Z", gmtime $t);
	$self->{kbrpc_tag} = "C:$0:$self->{hostname}:$$:$ts";
    }
    push(@{$self->{headers}}, 'Kbrpc-Tag', $self->{kbrpc_tag});

    if ($ENV{KBRPC_METADATA})
    {
	$self->{kbrpc_metadata} = $ENV{KBRPC_METADATA};
	push(@{$self->{headers}}, 'Kbrpc-Metadata', $self->{kbrpc_metadata});
    }

    if ($ENV{KBRPC_ERROR_DEST})
    {
	$self->{kbrpc_error_dest} = $ENV{KBRPC_ERROR_DEST};
	push(@{$self->{headers}}, 'Kbrpc-Errordest', $self->{kbrpc_error_dest});
    }

    #
    # This module requires authentication.
    #
    # We create an auth token, passing through the arguments that we were (hopefully) given.

    {
	my %arg_hash2 = @args;
	if (exists $arg_hash2{"token"}) {
	    $self->{token} = $arg_hash2{"token"};
	} elsif (exists $arg_hash2{"user_id"}) {
	    my $token = Bio::KBase::AuthToken->new(@args);
	    if (!$token->error_message) {
	        $self->{token} = $token->token;
	    }
	}
	
	if (exists $self->{token})
	{
	    $self->{client}->{token} = $self->{token};
	}
    }

    my $ua = $self->{client}->ua;	 
    my $timeout = $ENV{CDMI_TIMEOUT} || (30 * 60);	 
    $ua->timeout($timeout);
    bless $self, $class;
    #    $self->_validate_version();
    return $self;
}




=head2 get_parent

  $return = $obj->get_parent($ref)

=over 4

=item Parameter and return types

=begin html

<pre>
$ref is a TaxonAPI.ObjectReference
$return is a TaxonAPI.ObjectReference
ObjectReference is a string

</pre>

=end html

=begin text

$ref is a TaxonAPI.ObjectReference
$return is a TaxonAPI.ObjectReference
ObjectReference is a string


=end text

=item Description

Retrieve parent Taxon.

@return Reference to parent Taxon.

=back

=cut

 sub get_parent
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_parent (received $n, expecting 1)");
    }
    {
	my($ref) = @args;

	my @_bad_arguments;
        (!ref($ref)) or push(@_bad_arguments, "Invalid type for argument 1 \"ref\" (value was \"$ref\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_parent:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_parent');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_parent",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_parent',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_parent",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_parent',
				       );
    }
}
 


=head2 get_children

  $return = $obj->get_children($ref)

=over 4

=item Parameter and return types

=begin html

<pre>
$ref is a TaxonAPI.ObjectReference
$return is a reference to a list where each element is a TaxonAPI.ObjectReference
ObjectReference is a string

</pre>

=end html

=begin text

$ref is a TaxonAPI.ObjectReference
$return is a reference to a list where each element is a TaxonAPI.ObjectReference
ObjectReference is a string


=end text

=item Description

Retrieve children Taxon.

@return List of references to child Taxons.

=back

=cut

 sub get_children
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_children (received $n, expecting 1)");
    }
    {
	my($ref) = @args;

	my @_bad_arguments;
        (!ref($ref)) or push(@_bad_arguments, "Invalid type for argument 1 \"ref\" (value was \"$ref\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_children:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_children');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_children",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_children',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_children",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_children',
				       );
    }
}
 


=head2 get_genome_annotations

  $return = $obj->get_genome_annotations($ref)

=over 4

=item Parameter and return types

=begin html

<pre>
$ref is a TaxonAPI.ObjectReference
$return is a reference to a list where each element is a TaxonAPI.ObjectReference
ObjectReference is a string

</pre>

=end html

=begin text

$ref is a TaxonAPI.ObjectReference
$return is a reference to a list where each element is a TaxonAPI.ObjectReference
ObjectReference is a string


=end text

=item Description

funcdef GenomeAnnotation(s) that refer to this Taxon.
 If this is accessing a KBaseGenomes.Genome object, it will
 return an empty list (this information is not available).

 @return List of references to GenomeAnnotation objects.

=back

=cut

 sub get_genome_annotations
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_genome_annotations (received $n, expecting 1)");
    }
    {
	my($ref) = @args;

	my @_bad_arguments;
        (!ref($ref)) or push(@_bad_arguments, "Invalid type for argument 1 \"ref\" (value was \"$ref\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_genome_annotations:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_genome_annotations');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_genome_annotations",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_genome_annotations',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_genome_annotations",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_genome_annotations',
				       );
    }
}
 


=head2 get_scientific_lineage

  $return = $obj->get_scientific_lineage($ref)

=over 4

=item Parameter and return types

=begin html

<pre>
$ref is a TaxonAPI.ObjectReference
$return is a reference to a list where each element is a string
ObjectReference is a string

</pre>

=end html

=begin text

$ref is a TaxonAPI.ObjectReference
$return is a reference to a list where each element is a string
ObjectReference is a string


=end text

=item Description

Retrieve the scientific lineage.

@return Strings for each 'unit' of the lineage, ordered in
  the usual way from Domain to Kingdom to Phylum, etc.

=back

=cut

 sub get_scientific_lineage
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_scientific_lineage (received $n, expecting 1)");
    }
    {
	my($ref) = @args;

	my @_bad_arguments;
        (!ref($ref)) or push(@_bad_arguments, "Invalid type for argument 1 \"ref\" (value was \"$ref\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_scientific_lineage:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_scientific_lineage');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_scientific_lineage",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_scientific_lineage',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_scientific_lineage",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_scientific_lineage',
				       );
    }
}
 


=head2 get_scientific_name

  $return = $obj->get_scientific_name($ref)

=over 4

=item Parameter and return types

=begin html

<pre>
$ref is a TaxonAPI.ObjectReference
$return is a string
ObjectReference is a string

</pre>

=end html

=begin text

$ref is a TaxonAPI.ObjectReference
$return is a string
ObjectReference is a string


=end text

=item Description

Retrieve the scientific name.

@return The scientific name, e.g., "Escherichia Coli K12 str. MG1655"

=back

=cut

 sub get_scientific_name
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_scientific_name (received $n, expecting 1)");
    }
    {
	my($ref) = @args;

	my @_bad_arguments;
        (!ref($ref)) or push(@_bad_arguments, "Invalid type for argument 1 \"ref\" (value was \"$ref\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_scientific_name:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_scientific_name');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_scientific_name",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_scientific_name',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_scientific_name",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_scientific_name',
				       );
    }
}
 


=head2 get_taxonomic_id

  $return = $obj->get_taxonomic_id($ref)

=over 4

=item Parameter and return types

=begin html

<pre>
$ref is a TaxonAPI.ObjectReference
$return is an int
ObjectReference is a string

</pre>

=end html

=begin text

$ref is a TaxonAPI.ObjectReference
$return is an int
ObjectReference is a string


=end text

=item Description

Retrieve the NCBI taxonomic ID of this Taxon.
For type KBaseGenomes.Genome, the ``source_id`` will be returned.

@return Integer taxonomic ID.

=back

=cut

 sub get_taxonomic_id
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_taxonomic_id (received $n, expecting 1)");
    }
    {
	my($ref) = @args;

	my @_bad_arguments;
        (!ref($ref)) or push(@_bad_arguments, "Invalid type for argument 1 \"ref\" (value was \"$ref\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_taxonomic_id:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_taxonomic_id');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_taxonomic_id",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_taxonomic_id',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_taxonomic_id",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_taxonomic_id',
				       );
    }
}
 


=head2 get_kingdom

  $return = $obj->get_kingdom($ref)

=over 4

=item Parameter and return types

=begin html

<pre>
$ref is a TaxonAPI.ObjectReference
$return is a string
ObjectReference is a string

</pre>

=end html

=begin text

$ref is a TaxonAPI.ObjectReference
$return is a string
ObjectReference is a string


=end text

=item Description

Retrieve the kingdom.

=back

=cut

 sub get_kingdom
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_kingdom (received $n, expecting 1)");
    }
    {
	my($ref) = @args;

	my @_bad_arguments;
        (!ref($ref)) or push(@_bad_arguments, "Invalid type for argument 1 \"ref\" (value was \"$ref\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_kingdom:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_kingdom');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_kingdom",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_kingdom',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_kingdom",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_kingdom',
				       );
    }
}
 


=head2 get_domain

  $return = $obj->get_domain($ref)

=over 4

=item Parameter and return types

=begin html

<pre>
$ref is a TaxonAPI.ObjectReference
$return is a string
ObjectReference is a string

</pre>

=end html

=begin text

$ref is a TaxonAPI.ObjectReference
$return is a string
ObjectReference is a string


=end text

=item Description

Retrieve the domain.

=back

=cut

 sub get_domain
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_domain (received $n, expecting 1)");
    }
    {
	my($ref) = @args;

	my @_bad_arguments;
        (!ref($ref)) or push(@_bad_arguments, "Invalid type for argument 1 \"ref\" (value was \"$ref\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_domain:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_domain');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_domain",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_domain',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_domain",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_domain',
				       );
    }
}
 


=head2 get_genetic_code

  $return = $obj->get_genetic_code($ref)

=over 4

=item Parameter and return types

=begin html

<pre>
$ref is a TaxonAPI.ObjectReference
$return is an int
ObjectReference is a string

</pre>

=end html

=begin text

$ref is a TaxonAPI.ObjectReference
$return is an int
ObjectReference is a string


=end text

=item Description

Retrieve the genetic code.

=back

=cut

 sub get_genetic_code
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_genetic_code (received $n, expecting 1)");
    }
    {
	my($ref) = @args;

	my @_bad_arguments;
        (!ref($ref)) or push(@_bad_arguments, "Invalid type for argument 1 \"ref\" (value was \"$ref\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_genetic_code:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_genetic_code');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_genetic_code",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_genetic_code',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_genetic_code",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_genetic_code',
				       );
    }
}
 


=head2 get_aliases

  $return = $obj->get_aliases($ref)

=over 4

=item Parameter and return types

=begin html

<pre>
$ref is a TaxonAPI.ObjectReference
$return is a reference to a list where each element is a string
ObjectReference is a string

</pre>

=end html

=begin text

$ref is a TaxonAPI.ObjectReference
$return is a reference to a list where each element is a string
ObjectReference is a string


=end text

=item Description

Retrieve the aliases.

=back

=cut

 sub get_aliases
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_aliases (received $n, expecting 1)");
    }
    {
	my($ref) = @args;

	my @_bad_arguments;
        (!ref($ref)) or push(@_bad_arguments, "Invalid type for argument 1 \"ref\" (value was \"$ref\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_aliases:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_aliases');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_aliases",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_aliases',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_aliases",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_aliases',
				       );
    }
}
 


=head2 get_info

  $return = $obj->get_info($ref)

=over 4

=item Parameter and return types

=begin html

<pre>
$ref is a TaxonAPI.ObjectReference
$return is a TaxonAPI.ObjectInfo
ObjectReference is a string
ObjectInfo is a reference to a hash where the following keys are defined:
	object_id has a value which is an int
	object_name has a value which is a string
	object_reference has a value which is a string
	object_reference_versioned has a value which is a string
	type_string has a value which is a string
	save_date has a value which is a string
	version has a value which is an int
	saved_by has a value which is a string
	workspace_id has a value which is an int
	workspace_name has a value which is a string
	object_checksum has a value which is a string
	object_size has a value which is an int
	object_metadata has a value which is a reference to a hash where the key is a string and the value is a string

</pre>

=end html

=begin text

$ref is a TaxonAPI.ObjectReference
$return is a TaxonAPI.ObjectInfo
ObjectReference is a string
ObjectInfo is a reference to a hash where the following keys are defined:
	object_id has a value which is an int
	object_name has a value which is a string
	object_reference has a value which is a string
	object_reference_versioned has a value which is a string
	type_string has a value which is a string
	save_date has a value which is a string
	version has a value which is an int
	saved_by has a value which is a string
	workspace_id has a value which is an int
	workspace_name has a value which is a string
	object_checksum has a value which is a string
	object_size has a value which is an int
	object_metadata has a value which is a reference to a hash where the key is a string and the value is a string


=end text

=item Description

Retrieve object info.
@skip documentation

=back

=cut

 sub get_info
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_info (received $n, expecting 1)");
    }
    {
	my($ref) = @args;

	my @_bad_arguments;
        (!ref($ref)) or push(@_bad_arguments, "Invalid type for argument 1 \"ref\" (value was \"$ref\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_info:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_info');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_info",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_info',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_info",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_info',
				       );
    }
}
 


=head2 get_history

  $return = $obj->get_history($ref)

=over 4

=item Parameter and return types

=begin html

<pre>
$ref is a TaxonAPI.ObjectReference
$return is a TaxonAPI.ObjectHistory
ObjectReference is a string
ObjectHistory is a reference to a list where each element is a TaxonAPI.ObjectInfo
ObjectInfo is a reference to a hash where the following keys are defined:
	object_id has a value which is an int
	object_name has a value which is a string
	object_reference has a value which is a string
	object_reference_versioned has a value which is a string
	type_string has a value which is a string
	save_date has a value which is a string
	version has a value which is an int
	saved_by has a value which is a string
	workspace_id has a value which is an int
	workspace_name has a value which is a string
	object_checksum has a value which is a string
	object_size has a value which is an int
	object_metadata has a value which is a reference to a hash where the key is a string and the value is a string

</pre>

=end html

=begin text

$ref is a TaxonAPI.ObjectReference
$return is a TaxonAPI.ObjectHistory
ObjectReference is a string
ObjectHistory is a reference to a list where each element is a TaxonAPI.ObjectInfo
ObjectInfo is a reference to a hash where the following keys are defined:
	object_id has a value which is an int
	object_name has a value which is a string
	object_reference has a value which is a string
	object_reference_versioned has a value which is a string
	type_string has a value which is a string
	save_date has a value which is a string
	version has a value which is an int
	saved_by has a value which is a string
	workspace_id has a value which is an int
	workspace_name has a value which is a string
	object_checksum has a value which is a string
	object_size has a value which is an int
	object_metadata has a value which is a reference to a hash where the key is a string and the value is a string


=end text

=item Description

Retrieve object history.
@skip documentation

=back

=cut

 sub get_history
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_history (received $n, expecting 1)");
    }
    {
	my($ref) = @args;

	my @_bad_arguments;
        (!ref($ref)) or push(@_bad_arguments, "Invalid type for argument 1 \"ref\" (value was \"$ref\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_history:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_history');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_history",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_history',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_history",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_history',
				       );
    }
}
 


=head2 get_provenance

  $return = $obj->get_provenance($ref)

=over 4

=item Parameter and return types

=begin html

<pre>
$ref is a TaxonAPI.ObjectReference
$return is a TaxonAPI.ObjectProvenance
ObjectReference is a string
ObjectProvenance is a reference to a list where each element is a TaxonAPI.ObjectProvenanceAction
ObjectProvenanceAction is a reference to a hash where the following keys are defined:
	time has a value which is a string
	service_name has a value which is a string
	service_version has a value which is a string
	service_method has a value which is a string
	method_parameters has a value which is a reference to a list where each element is a string
	script_name has a value which is a string
	script_version has a value which is a string
	script_command_line has a value which is a string
	input_object_references has a value which is a reference to a list where each element is a string
	validated_object_references has a value which is a reference to a list where each element is a string
	intermediate_input_ids has a value which is a reference to a list where each element is a string
	intermediate_output_ids has a value which is a reference to a list where each element is a string
	external_data has a value which is a reference to a list where each element is a TaxonAPI.ExternalDataUnit
	description has a value which is a string
ExternalDataUnit is a reference to a hash where the following keys are defined:
	resource_name has a value which is a string
	resource_url has a value which is a string
	resource_version has a value which is a string
	resource_release_date has a value which is a string
	data_url has a value which is a string
	data_id has a value which is a string
	description has a value which is a string

</pre>

=end html

=begin text

$ref is a TaxonAPI.ObjectReference
$return is a TaxonAPI.ObjectProvenance
ObjectReference is a string
ObjectProvenance is a reference to a list where each element is a TaxonAPI.ObjectProvenanceAction
ObjectProvenanceAction is a reference to a hash where the following keys are defined:
	time has a value which is a string
	service_name has a value which is a string
	service_version has a value which is a string
	service_method has a value which is a string
	method_parameters has a value which is a reference to a list where each element is a string
	script_name has a value which is a string
	script_version has a value which is a string
	script_command_line has a value which is a string
	input_object_references has a value which is a reference to a list where each element is a string
	validated_object_references has a value which is a reference to a list where each element is a string
	intermediate_input_ids has a value which is a reference to a list where each element is a string
	intermediate_output_ids has a value which is a reference to a list where each element is a string
	external_data has a value which is a reference to a list where each element is a TaxonAPI.ExternalDataUnit
	description has a value which is a string
ExternalDataUnit is a reference to a hash where the following keys are defined:
	resource_name has a value which is a string
	resource_url has a value which is a string
	resource_version has a value which is a string
	resource_release_date has a value which is a string
	data_url has a value which is a string
	data_id has a value which is a string
	description has a value which is a string


=end text

=item Description

Retrieve object provenance.
@skip documentation

=back

=cut

 sub get_provenance
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_provenance (received $n, expecting 1)");
    }
    {
	my($ref) = @args;

	my @_bad_arguments;
        (!ref($ref)) or push(@_bad_arguments, "Invalid type for argument 1 \"ref\" (value was \"$ref\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_provenance:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_provenance');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_provenance",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_provenance',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_provenance",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_provenance',
				       );
    }
}
 


=head2 get_id

  $return = $obj->get_id($ref)

=over 4

=item Parameter and return types

=begin html

<pre>
$ref is a TaxonAPI.ObjectReference
$return is an int
ObjectReference is a string

</pre>

=end html

=begin text

$ref is a TaxonAPI.ObjectReference
$return is an int
ObjectReference is a string


=end text

=item Description

Retrieve object identifier.
@skip documentation

=back

=cut

 sub get_id
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_id (received $n, expecting 1)");
    }
    {
	my($ref) = @args;

	my @_bad_arguments;
        (!ref($ref)) or push(@_bad_arguments, "Invalid type for argument 1 \"ref\" (value was \"$ref\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_id:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_id');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_id",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_id',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_id",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_id',
				       );
    }
}
 


=head2 get_name

  $return = $obj->get_name($ref)

=over 4

=item Parameter and return types

=begin html

<pre>
$ref is a TaxonAPI.ObjectReference
$return is a string
ObjectReference is a string

</pre>

=end html

=begin text

$ref is a TaxonAPI.ObjectReference
$return is a string
ObjectReference is a string


=end text

=item Description

Retrieve object name.
@skip documentation

=back

=cut

 sub get_name
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_name (received $n, expecting 1)");
    }
    {
	my($ref) = @args;

	my @_bad_arguments;
        (!ref($ref)) or push(@_bad_arguments, "Invalid type for argument 1 \"ref\" (value was \"$ref\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_name:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_name');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_name",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_name',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_name",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_name',
				       );
    }
}
 


=head2 get_version

  $return = $obj->get_version($ref)

=over 4

=item Parameter and return types

=begin html

<pre>
$ref is a TaxonAPI.ObjectReference
$return is a string
ObjectReference is a string

</pre>

=end html

=begin text

$ref is a TaxonAPI.ObjectReference
$return is a string
ObjectReference is a string


=end text

=item Description

Retrieve object version.
@skip documentation

=back

=cut

 sub get_version
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_version (received $n, expecting 1)");
    }
    {
	my($ref) = @args;

	my @_bad_arguments;
        (!ref($ref)) or push(@_bad_arguments, "Invalid type for argument 1 \"ref\" (value was \"$ref\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_version:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_version');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_version",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_version',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_version",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_version',
				       );
    }
}
 


=head2 get_all_data

  $d = $obj->get_all_data($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a TaxonAPI.GetAllDataParams
$d is a TaxonAPI.TaxonData
GetAllDataParams is a reference to a hash where the following keys are defined:
	ref has a value which is a TaxonAPI.ObjectReference
	include_decorated_scientific_lineage has a value which is a TaxonAPI.boolean
	include_decorated_children has a value which is a TaxonAPI.boolean
	exclude_children has a value which is a TaxonAPI.boolean
ObjectReference is a string
boolean is an int
TaxonData is a reference to a hash where the following keys are defined:
	parent has a value which is a TaxonAPI.ObjectReference
	children has a value which is a reference to a list where each element is a TaxonAPI.ObjectReference
	decorated_children has a value which is a reference to a list where each element is a TaxonAPI.TaxonInfo
	scientific_lineage has a value which is a reference to a list where each element is a string
	decorated_scientific_lineage has a value which is a reference to a list where each element is a TaxonAPI.TaxonInfo
	scientific_name has a value which is a string
	taxonomic_id has a value which is an int
	kingdom has a value which is a string
	domain has a value which is a string
	genetic_code has a value which is an int
	aliases has a value which is a reference to a list where each element is a string
	obj_info has a value which is a TaxonAPI.ObjectInfo
TaxonInfo is a reference to a hash where the following keys are defined:
	ref has a value which is a TaxonAPI.ObjectReference
	scientific_name has a value which is a string
ObjectInfo is a reference to a hash where the following keys are defined:
	object_id has a value which is an int
	object_name has a value which is a string
	object_reference has a value which is a string
	object_reference_versioned has a value which is a string
	type_string has a value which is a string
	save_date has a value which is a string
	version has a value which is an int
	saved_by has a value which is a string
	workspace_id has a value which is an int
	workspace_name has a value which is a string
	object_checksum has a value which is a string
	object_size has a value which is an int
	object_metadata has a value which is a reference to a hash where the key is a string and the value is a string

</pre>

=end html

=begin text

$params is a TaxonAPI.GetAllDataParams
$d is a TaxonAPI.TaxonData
GetAllDataParams is a reference to a hash where the following keys are defined:
	ref has a value which is a TaxonAPI.ObjectReference
	include_decorated_scientific_lineage has a value which is a TaxonAPI.boolean
	include_decorated_children has a value which is a TaxonAPI.boolean
	exclude_children has a value which is a TaxonAPI.boolean
ObjectReference is a string
boolean is an int
TaxonData is a reference to a hash where the following keys are defined:
	parent has a value which is a TaxonAPI.ObjectReference
	children has a value which is a reference to a list where each element is a TaxonAPI.ObjectReference
	decorated_children has a value which is a reference to a list where each element is a TaxonAPI.TaxonInfo
	scientific_lineage has a value which is a reference to a list where each element is a string
	decorated_scientific_lineage has a value which is a reference to a list where each element is a TaxonAPI.TaxonInfo
	scientific_name has a value which is a string
	taxonomic_id has a value which is an int
	kingdom has a value which is a string
	domain has a value which is a string
	genetic_code has a value which is an int
	aliases has a value which is a reference to a list where each element is a string
	obj_info has a value which is a TaxonAPI.ObjectInfo
TaxonInfo is a reference to a hash where the following keys are defined:
	ref has a value which is a TaxonAPI.ObjectReference
	scientific_name has a value which is a string
ObjectInfo is a reference to a hash where the following keys are defined:
	object_id has a value which is an int
	object_name has a value which is a string
	object_reference has a value which is a string
	object_reference_versioned has a value which is a string
	type_string has a value which is a string
	save_date has a value which is a string
	version has a value which is an int
	saved_by has a value which is a string
	workspace_id has a value which is an int
	workspace_name has a value which is a string
	object_checksum has a value which is a string
	object_size has a value which is an int
	object_metadata has a value which is a reference to a hash where the key is a string and the value is a string


=end text

=item Description



=back

=cut

 sub get_all_data
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_all_data (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_all_data:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_all_data');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_all_data",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_all_data',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_all_data",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_all_data',
				       );
    }
}
 


=head2 get_decorated_scientific_lineage

  $return = $obj->get_decorated_scientific_lineage($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a TaxonAPI.GetDecoratedScientificLineageParams
$return is a TaxonAPI.DecoratedScientificLineage
GetDecoratedScientificLineageParams is a reference to a hash where the following keys are defined:
	ref has a value which is a TaxonAPI.ObjectReference
ObjectReference is a string
DecoratedScientificLineage is a reference to a hash where the following keys are defined:
	decorated_scientific_lineage has a value which is a reference to a list where each element is a TaxonAPI.TaxonInfo
TaxonInfo is a reference to a hash where the following keys are defined:
	ref has a value which is a TaxonAPI.ObjectReference
	scientific_name has a value which is a string

</pre>

=end html

=begin text

$params is a TaxonAPI.GetDecoratedScientificLineageParams
$return is a TaxonAPI.DecoratedScientificLineage
GetDecoratedScientificLineageParams is a reference to a hash where the following keys are defined:
	ref has a value which is a TaxonAPI.ObjectReference
ObjectReference is a string
DecoratedScientificLineage is a reference to a hash where the following keys are defined:
	decorated_scientific_lineage has a value which is a reference to a list where each element is a TaxonAPI.TaxonInfo
TaxonInfo is a reference to a hash where the following keys are defined:
	ref has a value which is a TaxonAPI.ObjectReference
	scientific_name has a value which is a string


=end text

=item Description



=back

=cut

 sub get_decorated_scientific_lineage
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_decorated_scientific_lineage (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_decorated_scientific_lineage:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_decorated_scientific_lineage');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_decorated_scientific_lineage",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_decorated_scientific_lineage',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_decorated_scientific_lineage",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_decorated_scientific_lineage',
				       );
    }
}
 


=head2 get_decorated_children

  $return = $obj->get_decorated_children($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a TaxonAPI.GetDecoratedChildrenParams
$return is a TaxonAPI.DecoratedChildren
GetDecoratedChildrenParams is a reference to a hash where the following keys are defined:
	ref has a value which is a TaxonAPI.ObjectReference
ObjectReference is a string
DecoratedChildren is a reference to a hash where the following keys are defined:
	decorated_children has a value which is a reference to a list where each element is a TaxonAPI.TaxonInfo
TaxonInfo is a reference to a hash where the following keys are defined:
	ref has a value which is a TaxonAPI.ObjectReference
	scientific_name has a value which is a string

</pre>

=end html

=begin text

$params is a TaxonAPI.GetDecoratedChildrenParams
$return is a TaxonAPI.DecoratedChildren
GetDecoratedChildrenParams is a reference to a hash where the following keys are defined:
	ref has a value which is a TaxonAPI.ObjectReference
ObjectReference is a string
DecoratedChildren is a reference to a hash where the following keys are defined:
	decorated_children has a value which is a reference to a list where each element is a TaxonAPI.TaxonInfo
TaxonInfo is a reference to a hash where the following keys are defined:
	ref has a value which is a TaxonAPI.ObjectReference
	scientific_name has a value which is a string


=end text

=item Description



=back

=cut

 sub get_decorated_children
{
    my($self, @args) = @_;

# Authentication: optional

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_decorated_children (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_decorated_children:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_decorated_children');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "TaxonAPI.get_decorated_children",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_decorated_children',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_decorated_children",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_decorated_children',
				       );
    }
}
 
  
sub status
{
    my($self, @args) = @_;
    if ((my $n = @args) != 0) {
        Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
                                   "Invalid argument count for function status (received $n, expecting 0)");
    }
    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
        method => "TaxonAPI.status",
        params => \@args,
    });
    if ($result) {
        if ($result->is_error) {
            Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
                           code => $result->content->{error}->{code},
                           method_name => 'status',
                           data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
                          );
        } else {
            return wantarray ? @{$result->result} : $result->result->[0];
        }
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method status",
                        status_line => $self->{client}->status_line,
                        method_name => 'status',
                       );
    }
}
   

sub version {
    my ($self) = @_;
    my $result = $self->{client}->call($self->{url}, $self->{headers}, {
        method => "TaxonAPI.version",
        params => [],
    });
    if ($result) {
        if ($result->is_error) {
            Bio::KBase::Exceptions::JSONRPC->throw(
                error => $result->error_message,
                code => $result->content->{code},
                method_name => 'get_decorated_children',
            );
        } else {
            return wantarray ? @{$result->result} : $result->result->[0];
        }
    } else {
        Bio::KBase::Exceptions::HTTP->throw(
            error => "Error invoking method get_decorated_children",
            status_line => $self->{client}->status_line,
            method_name => 'get_decorated_children',
        );
    }
}

sub _validate_version {
    my ($self) = @_;
    my $svr_version = $self->version();
    my $client_version = $VERSION;
    my ($cMajor, $cMinor) = split(/\./, $client_version);
    my ($sMajor, $sMinor) = split(/\./, $svr_version);
    if ($sMajor != $cMajor) {
        Bio::KBase::Exceptions::ClientServerIncompatible->throw(
            error => "Major version numbers differ.",
            server_version => $svr_version,
            client_version => $client_version
        );
    }
    if ($sMinor < $cMinor) {
        Bio::KBase::Exceptions::ClientServerIncompatible->throw(
            error => "Client minor version greater than Server minor version.",
            server_version => $svr_version,
            client_version => $client_version
        );
    }
    if ($sMinor > $cMinor) {
        warn "New client version available for TaxonAPI::TaxonAPIClient\n";
    }
    if ($sMajor == 0) {
        warn "TaxonAPI::TaxonAPIClient version is $svr_version. API subject to change.\n";
    }
}

=head1 TYPES



=head2 boolean

=over 4



=item Description

A boolean. 0 = false, other = true.


=item Definition

=begin html

<pre>
an int
</pre>

=end html

=begin text

an int

=end text

=back



=head2 ObjectReference

=over 4



=item Definition

=begin html

<pre>
a string
</pre>

=end html

=begin text

a string

=end text

=back



=head2 ObjectInfo

=over 4



=item Description

* @skip documentation


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
object_id has a value which is an int
object_name has a value which is a string
object_reference has a value which is a string
object_reference_versioned has a value which is a string
type_string has a value which is a string
save_date has a value which is a string
version has a value which is an int
saved_by has a value which is a string
workspace_id has a value which is an int
workspace_name has a value which is a string
object_checksum has a value which is a string
object_size has a value which is an int
object_metadata has a value which is a reference to a hash where the key is a string and the value is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
object_id has a value which is an int
object_name has a value which is a string
object_reference has a value which is a string
object_reference_versioned has a value which is a string
type_string has a value which is a string
save_date has a value which is a string
version has a value which is an int
saved_by has a value which is a string
workspace_id has a value which is an int
workspace_name has a value which is a string
object_checksum has a value which is a string
object_size has a value which is an int
object_metadata has a value which is a reference to a hash where the key is a string and the value is a string


=end text

=back



=head2 ObjectHistory

=over 4



=item Description

* @skip documentation


=item Definition

=begin html

<pre>
a reference to a list where each element is a TaxonAPI.ObjectInfo
</pre>

=end html

=begin text

a reference to a list where each element is a TaxonAPI.ObjectInfo

=end text

=back



=head2 ExternalDataUnit

=over 4



=item Description

* @skip documentation


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
resource_name has a value which is a string
resource_url has a value which is a string
resource_version has a value which is a string
resource_release_date has a value which is a string
data_url has a value which is a string
data_id has a value which is a string
description has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
resource_name has a value which is a string
resource_url has a value which is a string
resource_version has a value which is a string
resource_release_date has a value which is a string
data_url has a value which is a string
data_id has a value which is a string
description has a value which is a string


=end text

=back



=head2 ObjectProvenanceAction

=over 4



=item Description

* @skip documentation


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
time has a value which is a string
service_name has a value which is a string
service_version has a value which is a string
service_method has a value which is a string
method_parameters has a value which is a reference to a list where each element is a string
script_name has a value which is a string
script_version has a value which is a string
script_command_line has a value which is a string
input_object_references has a value which is a reference to a list where each element is a string
validated_object_references has a value which is a reference to a list where each element is a string
intermediate_input_ids has a value which is a reference to a list where each element is a string
intermediate_output_ids has a value which is a reference to a list where each element is a string
external_data has a value which is a reference to a list where each element is a TaxonAPI.ExternalDataUnit
description has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
time has a value which is a string
service_name has a value which is a string
service_version has a value which is a string
service_method has a value which is a string
method_parameters has a value which is a reference to a list where each element is a string
script_name has a value which is a string
script_version has a value which is a string
script_command_line has a value which is a string
input_object_references has a value which is a reference to a list where each element is a string
validated_object_references has a value which is a reference to a list where each element is a string
intermediate_input_ids has a value which is a reference to a list where each element is a string
intermediate_output_ids has a value which is a reference to a list where each element is a string
external_data has a value which is a reference to a list where each element is a TaxonAPI.ExternalDataUnit
description has a value which is a string


=end text

=back



=head2 ObjectProvenance

=over 4



=item Description

* @skip documentation


=item Definition

=begin html

<pre>
a reference to a list where each element is a TaxonAPI.ObjectProvenanceAction
</pre>

=end html

=begin text

a reference to a list where each element is a TaxonAPI.ObjectProvenanceAction

=end text

=back



=head2 GetAllDataParams

=over 4



=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
ref has a value which is a TaxonAPI.ObjectReference
include_decorated_scientific_lineage has a value which is a TaxonAPI.boolean
include_decorated_children has a value which is a TaxonAPI.boolean
exclude_children has a value which is a TaxonAPI.boolean

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
ref has a value which is a TaxonAPI.ObjectReference
include_decorated_scientific_lineage has a value which is a TaxonAPI.boolean
include_decorated_children has a value which is a TaxonAPI.boolean
exclude_children has a value which is a TaxonAPI.boolean


=end text

=back



=head2 TaxonInfo

=over 4



=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
ref has a value which is a TaxonAPI.ObjectReference
scientific_name has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
ref has a value which is a TaxonAPI.ObjectReference
scientific_name has a value which is a string


=end text

=back



=head2 TaxonData

=over 4



=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
parent has a value which is a TaxonAPI.ObjectReference
children has a value which is a reference to a list where each element is a TaxonAPI.ObjectReference
decorated_children has a value which is a reference to a list where each element is a TaxonAPI.TaxonInfo
scientific_lineage has a value which is a reference to a list where each element is a string
decorated_scientific_lineage has a value which is a reference to a list where each element is a TaxonAPI.TaxonInfo
scientific_name has a value which is a string
taxonomic_id has a value which is an int
kingdom has a value which is a string
domain has a value which is a string
genetic_code has a value which is an int
aliases has a value which is a reference to a list where each element is a string
obj_info has a value which is a TaxonAPI.ObjectInfo

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
parent has a value which is a TaxonAPI.ObjectReference
children has a value which is a reference to a list where each element is a TaxonAPI.ObjectReference
decorated_children has a value which is a reference to a list where each element is a TaxonAPI.TaxonInfo
scientific_lineage has a value which is a reference to a list where each element is a string
decorated_scientific_lineage has a value which is a reference to a list where each element is a TaxonAPI.TaxonInfo
scientific_name has a value which is a string
taxonomic_id has a value which is an int
kingdom has a value which is a string
domain has a value which is a string
genetic_code has a value which is an int
aliases has a value which is a reference to a list where each element is a string
obj_info has a value which is a TaxonAPI.ObjectInfo


=end text

=back



=head2 GetDecoratedScientificLineageParams

=over 4



=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
ref has a value which is a TaxonAPI.ObjectReference

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
ref has a value which is a TaxonAPI.ObjectReference


=end text

=back



=head2 DecoratedScientificLineage

=over 4



=item Description

list starts at the root, and goes on down to this


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
decorated_scientific_lineage has a value which is a reference to a list where each element is a TaxonAPI.TaxonInfo

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
decorated_scientific_lineage has a value which is a reference to a list where each element is a TaxonAPI.TaxonInfo


=end text

=back



=head2 GetDecoratedChildrenParams

=over 4



=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
ref has a value which is a TaxonAPI.ObjectReference

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
ref has a value which is a TaxonAPI.ObjectReference


=end text

=back



=head2 DecoratedChildren

=over 4



=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
decorated_children has a value which is a reference to a list where each element is a TaxonAPI.TaxonInfo

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
decorated_children has a value which is a reference to a list where each element is a TaxonAPI.TaxonInfo


=end text

=back



=cut

package TaxonAPI::TaxonAPIClient::RpcClient;
use base 'JSON::RPC::Client';
use POSIX;
use strict;

#
# Override JSON::RPC::Client::call because it doesn't handle error returns properly.
#

sub call {
    my ($self, $uri, $headers, $obj) = @_;
    my $result;


    {
	if ($uri =~ /\?/) {
	    $result = $self->_get($uri);
	}
	else {
	    Carp::croak "not hashref." unless (ref $obj eq 'HASH');
	    $result = $self->_post($uri, $headers, $obj);
	}

    }

    my $service = $obj->{method} =~ /^system\./ if ( $obj );

    $self->status_line($result->status_line);

    if ($result->is_success) {

        return unless($result->content); # notification?

        if ($service) {
            return JSON::RPC::ServiceObject->new($result, $self->json);
        }

        return JSON::RPC::ReturnObject->new($result, $self->json);
    }
    elsif ($result->content_type eq 'application/json')
    {
        return JSON::RPC::ReturnObject->new($result, $self->json);
    }
    else {
        return;
    }
}


sub _post {
    my ($self, $uri, $headers, $obj) = @_;
    my $json = $self->json;

    $obj->{version} ||= $self->{version} || '1.1';

    if ($obj->{version} eq '1.0') {
        delete $obj->{version};
        if (exists $obj->{id}) {
            $self->id($obj->{id}) if ($obj->{id}); # if undef, it is notification.
        }
        else {
            $obj->{id} = $self->id || ($self->id('JSON::RPC::Client'));
        }
    }
    else {
        # $obj->{id} = $self->id if (defined $self->id);
	# Assign a random number to the id if one hasn't been set
	$obj->{id} = (defined $self->id) ? $self->id : substr(rand(),2);
    }

    my $content = $json->encode($obj);

    $self->ua->post(
        $uri,
        Content_Type   => $self->{content_type},
        Content        => $content,
        Accept         => 'application/json',
	@$headers,
	($self->{token} ? (Authorization => $self->{token}) : ()),
    );
}



1;
