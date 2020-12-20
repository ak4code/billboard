def company_logo_directory_path(instance, filename):
    return f'companies/{instance.slug}/logo/{filename}'
