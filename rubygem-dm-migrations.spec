#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-dm-migrations
Version  : 1.2.0
Release  : 2
URL      : https://rubygems.org/downloads/dm-migrations-1.2.0.gem
Source0  : https://rubygems.org/downloads/dm-migrations-1.2.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-addressable
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-dm-core
BuildRequires : rubygem-jeweler
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-test-unit

%description
= dm-migrations
DataMapper plugin for writing and specing migrations.
== Example

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n dm-migrations-1.2.0
gem spec %{SOURCE0} -l --ruby > rubygem-dm-migrations.gemspec

%build
gem build rubygem-dm-migrations.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
dm-migrations-1.2.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/dm-migrations-1.2.0.gem
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Adapters/auto_migration_extensions-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Adapters/cdesc-Adapters.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Adapters/const_added-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Adapters/include_migration_api-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Adapters/migration_module-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/%3c%3d%3e-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/adapter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/cdesc-Migration.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/create_index-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/create_migration_info_table_if_needed-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/create_table-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/database-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/down-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/drop_table-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/execute-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/migration_info_table-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/migration_info_table_exists%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/migration_name_column-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/migration_record-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/modify_table-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/needs_down%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/needs_up%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/perform_down-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/perform_up-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/position-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/quote_column_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/quote_table_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/quoted_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/repository-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/say-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/say_with_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/setup%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/setup%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/up-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/update_migration_info-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migration/write-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/MigrationRunner/cdesc-MigrationRunner.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/MigrationRunner/migrate_down%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/MigrationRunner/migrate_up%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/MigrationRunner/migration-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/MigrationRunner/migrations-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/DataObjectsAdapter/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/DataObjectsAdapter/ClassMethods/type_map-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/DataObjectsAdapter/SQL/cdesc-SQL.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/DataObjectsAdapter/cdesc-DataObjectsAdapter.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/DataObjectsAdapter/create_model_storage-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/DataObjectsAdapter/destroy_model_storage-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/DataObjectsAdapter/field_exists%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/DataObjectsAdapter/storage_exists%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/DataObjectsAdapter/upgrade_model_storage-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/DuplicateMigration/cdesc-DuplicateMigration.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/Model/auto_migrate%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/Model/auto_migrate_down%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/Model/auto_migrate_up%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/Model/auto_upgrade%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/Model/cdesc-Model.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/Model/included-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/Model/storage_exists%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/MysqlAdapter/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/MysqlAdapter/ClassMethods/type_map-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/MysqlAdapter/SQL/cdesc-SQL.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/MysqlAdapter/cdesc-MysqlAdapter.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/MysqlAdapter/field_exists%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/MysqlAdapter/included-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/MysqlAdapter/storage_exists%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/OracleAdapter/ClassMethods/auto_migrate_reset_sequences-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/OracleAdapter/ClassMethods/auto_migrate_with-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/OracleAdapter/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/OracleAdapter/ClassMethods/type_map-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/OracleAdapter/SQL/cdesc-SQL.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/OracleAdapter/cdesc-OracleAdapter.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/OracleAdapter/create_model_storage-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/OracleAdapter/destroy_model_storage-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/OracleAdapter/drop_table_statement-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/OracleAdapter/field_exists%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/OracleAdapter/included-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/OracleAdapter/oracle_upcase-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/OracleAdapter/sequence_exists%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/OracleAdapter/storage_exists%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/OracleAdapter/storage_fields-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/OracleAdapter/storage_has_all_fields%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/PostgresAdapter/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/PostgresAdapter/ClassMethods/type_map-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/PostgresAdapter/SQL/cdesc-SQL.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/PostgresAdapter/cdesc-PostgresAdapter.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/PostgresAdapter/create_model_storage-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/PostgresAdapter/destroy_model_storage-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/PostgresAdapter/included-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/PostgresAdapter/upgrade_model_storage-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/Repository/auto_migrate%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/Repository/auto_upgrade%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/Repository/cdesc-Repository.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/Repository/create_model_storage-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/Repository/destroy_model_storage-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/Repository/storage_exists%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/Repository/upgrade_model_storage-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SingletonMethods/auto_migrate%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SingletonMethods/auto_migrate_down%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SingletonMethods/auto_migrate_up%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SingletonMethods/auto_upgrade%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SingletonMethods/cdesc-SingletonMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SingletonMethods/migrate%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SingletonMethods/repository_execute-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SqliteAdapter/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SqliteAdapter/ClassMethods/type_map-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SqliteAdapter/SQL/cdesc-SQL.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SqliteAdapter/cdesc-SqliteAdapter.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SqliteAdapter/field_exists%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SqliteAdapter/included-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SqliteAdapter/storage_exists%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SqlserverAdapter/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SqlserverAdapter/ClassMethods/type_map-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SqlserverAdapter/SQL/cdesc-SQL.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SqlserverAdapter/cdesc-SqlserverAdapter.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SqlserverAdapter/field_exists%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SqlserverAdapter/included-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/SqlserverAdapter/storage_exists%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/YamlAdapter/cdesc-YamlAdapter.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/YamlAdapter/destroy_model_storage-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/YamlAdapter/included-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/cdesc-Migrations.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/Migrations/include_migration_api-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/DataMapper/cdesc-DataMapper.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Column/cdesc-Column.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Column/default_value-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Column/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Column/not_null-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Column/primary_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Column/type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Column/unique-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Mysql/Column/cdesc-Column.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Mysql/Column/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Mysql/Table/cdesc-Table.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Mysql/Table/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Mysql/cdesc-Mysql.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Mysql/change_column_type_statement-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Mysql/property_schema_statement-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Mysql/recreate_database-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Mysql/supports_schema_transactions%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Mysql/supports_serial%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Mysql/table-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Mysql/table_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Postgres/Column/cdesc-Column.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Postgres/Column/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Postgres/Table/cdesc-Table.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Postgres/Table/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Postgres/Table/query_column_constraints-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Postgres/cdesc-Postgres.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Postgres/change_column_type_statement-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Postgres/property_schema_statement-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Postgres/recreate_database-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Postgres/supports_schema_transactions%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Postgres/supports_serial%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Postgres/table-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Postgres/table_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Sqlite/Column/cdesc-Column.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Sqlite/Column/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Sqlite/Table/cdesc-Table.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Sqlite/Table/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Sqlite/cdesc-Sqlite.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Sqlite/change_column_type_statement-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Sqlite/recreate_database-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Sqlite/supports_schema_transactions%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Sqlite/supports_serial%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Sqlite/table-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Sqlite/table_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Table/cdesc-Table.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Table/column-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Table/columns-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Table/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/Table/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/Column/build_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/Column/cdesc-Column.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/Column/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/Column/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/Column/quoted_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/Column/to_sql-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/Column/type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/SqlExpr/cdesc-SqlExpr.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/SqlExpr/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/SqlExpr/sql-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/SqlExpr/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/cdesc-TableCreator.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/column-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/now-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/opts-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/quoted_table_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/table_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/to_sql-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableCreator/uuid-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableModifier/adapter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableModifier/add_column-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableModifier/cdesc-TableModifier.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableModifier/change_column-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableModifier/drop_column-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableModifier/drop_columns-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableModifier/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableModifier/opts-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableModifier/quote_column_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableModifier/quoted_table_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableModifier/rename_column-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableModifier/statements-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableModifier/table_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/TableModifier/to_sql-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/SQL/cdesc-SQL.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Example/MigrationExampleGroup/all_databases-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Example/MigrationExampleGroup/cdesc-MigrationExampleGroup.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Example/MigrationExampleGroup/migration_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Example/MigrationExampleGroup/run_migration-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Example/MigrationExampleGroup/run_prereq_migrations-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Example/MigrationExampleGroup/select-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Example/MigrationExampleGroup/table-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Example/MigrationExampleGroup/this_migration-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Example/cdesc-Example.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/HaveColumnMatcher/cdesc-HaveColumnMatcher.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/HaveColumnMatcher/column_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/HaveColumnMatcher/failure_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/HaveColumnMatcher/matches%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/HaveColumnMatcher/negative_failure_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/HaveColumnMatcher/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/HaveColumnMatcher/table-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/HaveTableMatcher/cdesc-HaveTableMatcher.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/HaveTableMatcher/failure_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/HaveTableMatcher/matches%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/HaveTableMatcher/negative_failure_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/HaveTableMatcher/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/HaveTableMatcher/repository-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/HaveTableMatcher/table_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/NullableColumnMatcher/cdesc-NullableColumnMatcher.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/NullableColumnMatcher/column-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/NullableColumnMatcher/failure_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/NullableColumnMatcher/matches%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/NullableColumnMatcher/negative_failure_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/PrimaryKeyMatcher/cdesc-PrimaryKeyMatcher.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/PrimaryKeyMatcher/column-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/PrimaryKeyMatcher/failure_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/PrimaryKeyMatcher/matches%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/PrimaryKeyMatcher/negative_failure_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/be_primary_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/cdesc-Migration.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/have_column-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/have_table-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/Migration/permit_null-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/Matchers/cdesc-Matchers.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/Spec/cdesc-Spec.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/page-LICENSE.ri
/usr/lib64/ruby/gems/2.2.0/doc/dm-migrations-1.2.0/ri/page-README_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/README.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/VERSION
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/db/migrations/1_create_people_table.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/db/migrations/2_add_dob_to_people.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/db/migrations/config.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/dm-migrations.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/examples/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/examples/sample_migration.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/examples/sample_migration_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/adapters/dm-do-adapter.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/adapters/dm-mysql-adapter.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/adapters/dm-oracle-adapter.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/adapters/dm-postgres-adapter.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/adapters/dm-sqlite-adapter.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/adapters/dm-sqlserver-adapter.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/adapters/dm-yaml-adapter.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/auto_migration.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/exceptions/duplicate_migration.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/migration.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/migration_runner.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/sql.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/sql/column.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/sql/mysql.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/sql/postgres.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/sql/sqlite.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/sql/table.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/sql/table_creator.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/dm-migrations/sql/table_modifier.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/spec/example/migration_example_group.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/lib/spec/matchers/migration_matchers.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/integration/auto_migration_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/integration/auto_upgrade_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/integration/migration_runner_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/integration/migration_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/integration/sql_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/isolated/require_after_setup_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/isolated/require_before_setup_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/isolated/require_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/rcov.opts
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/spec.opts
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/unit/migration_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/unit/sql/column_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/unit/sql/postgres_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/unit/sql/sqlite_extensions_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/unit/sql/table_creator_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/unit/sql/table_modifier_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/unit/sql/table_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/spec/unit/sql_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/tasks/spec.rake
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/tasks/yard.rake
/usr/lib64/ruby/gems/2.2.0/gems/dm-migrations-1.2.0/tasks/yardstick.rake
/usr/lib64/ruby/gems/2.2.0/specifications/dm-migrations-1.2.0.gemspec
