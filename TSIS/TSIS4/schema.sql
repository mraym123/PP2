create table if not exists players(
    id serial primary key,
    username varchar(50) not null unique
);

create table if not exists game_sessions(
    id serial primary key,
    player_id integer references players(id) on delete cascade,
    score integer not null,
    level_reached integer not null,
    played_at timestamp default NOW()
);