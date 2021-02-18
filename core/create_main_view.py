def create_main_view(cur):
    cmd = """
create view if not exists main_view
as
    select 
        m.show_id,
        m.type,
        m.title,
        m_d.director,
        m_c.actors as 'cast',
        m_cntr.country,
        m.date_added,
        m.release_year,
        m.rating,
        m.duration,
        m.seasons,
        m_g.listed_in
    from Movies m
    left join (
        select id, group_concat(name, ', ') director 
        from Movie_directors
        group by id
    ) m_d on m.show_id = m_d.id
    left join (
        select id, group_concat(name, ', ') actors 
        from Movie_cast
        group by id
    ) m_c on m.show_id = m_c.id
    left join (
        select id, group_concat(name, ', ') country  
        from Movie_country
        group by id
    ) m_cntr on m.show_id = m_cntr.id
    left join (
        select id, group_concat(name, ', ') listed_in
        from Movie_genre
        group by id
    ) m_g on m.show_id = m_g.id
    group by m.show_id;
    
"""
    cur.execute(cmd)