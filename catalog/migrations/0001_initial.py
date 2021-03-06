# Generated by Django 2.0.3 on 2018-04-23 17:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True, help_text='Enter a brief description of the author', max_length=2000)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('call_no', models.CharField(blank=True, help_text='Enter the classification number of the book', max_length=200, verbose_name='Call number')),
                ('title', models.CharField(max_length=200)),
                ('series', models.CharField(blank=True, max_length=200)),
                ('desc', models.TextField(blank=True, default='No description available.', help_text='Enter a brief description of the book', max_length=2000)),
                ('isbn_13', models.CharField(help_text='Enter ISBN of the book', max_length=13, primary_key=True, serialize=False, verbose_name='ISBN-13')),
                ('img_url_s', models.URLField(default='/static/img/default.png', help_text='Enter the URL to book cover image (small)', verbose_name='Image URL (small)')),
                ('img_url_m', models.URLField(default='/static/img/default.png', help_text='Enter the URL to book cover image (medium)', verbose_name='Image URL (medium)')),
                ('img_url_l', models.URLField(default='/static/img/default.png', help_text='Enter the URL to book cover image (large)', verbose_name='Image URL (large)')),
                ('author', models.ManyToManyField(help_text='Select author for the book', to='catalog.Author')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library. Do not modify.', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('a', 'Available'), ('m', 'Maintenance'), ('o', 'On loan'), ('r', 'Reserved')], default='m', help_text='Book availability', max_length=1)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Book')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book genre', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the language of the book', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_coor', models.IntegerField()),
                ('y_coor', models.IntegerField()),
                ('book', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select genre(s) for the book', to='catalog.Genre'),
        ),
    ]
