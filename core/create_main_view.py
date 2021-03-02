def create_main_view(cur: "sqlite3.Cursor"):
    cmd = """
create view if not exists main_view
as
    select
        t1.show_id, t1.type, t1.title,
        group_concat(distinct t2.name) director,
        group_concat(distinct t3.name) as cast,
        group_concat(distinct t4.name) country,
        t1.date_added, t1.release_year, t1.rating, 
        case
            when t1.seasons = 1 then cast(t1.seasons as text) || ' Season'
            when t1.seasons > 1 then cast(t1.seasons as text) || ' Seasons'
            else cast(t1.duration as text) || ' min'
        end duration,
        group_concat(distinct t5.name) listed_in
    from
        Movies t1,
        Movie_directors t2,
        Movie_cast t3,
        Movie_country t4,
        Movie_genre t5
    where (t1.show_id, t1.show_id, t1.show_id, t1.show_id) = (t2.id, t3.id, t4.id, t5.id)
    group by t1.show_id;
"""
    cur.execute(cmd)