from dynamic_preferences import types
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry

clan_ranks = Section('clan_ranks')


@global_preferences_registry.register
class RecruitRank(types.FloatPreference):
    section = clan_ranks
    verbose_name = 'Exp para Recruta'
    name = 'recruit_exp'
    default = float(0)


@global_preferences_registry.register
class CorporalRank(types.FloatPreference):
    section = clan_ranks
    verbose_name = 'Exp para Cabo'
    name = 'corporal_exp'
    default = float(0)


@global_preferences_registry.register
class SergeantRank(types.FloatPreference):
    section = clan_ranks
    verbose_name = 'Exp para Sargento'
    name = 'sergeant_exp'
    default = float(50_000_000)


@global_preferences_registry.register
class LieutenantRank(types.FloatPreference):
    section = clan_ranks
    verbose_name = 'Exp para Tenente'
    name = 'lieutenant_exp'
    default = float(125_000_000)


@global_preferences_registry.register
class CaptainRank(types.FloatPreference):
    section = clan_ranks
    verbose_name = 'Exp para Capitão'
    name = 'captain_exp'
    default = float(225_000_000)


@global_preferences_registry.register
class GeneralRank(types.FloatPreference):
    section = clan_ranks
    verbose_name = 'Exp para General'
    name = 'general_exp'
    default = float(500_000_000)
