import unreal


def enum_member(enum_type, needle):
    for name in dir(enum_type):
        if needle in name.upper():
            return name, getattr(enum_type, name)
    return None, None


channel_name = "ECC_GAME_TRACE_CHANNEL1(6)"
player_channel = unreal.CollisionChannel(6)
unreal.log_warning(f"PLAYER_TRACE_ENUM={channel_name}:{player_channel}")

bp = unreal.load_asset("/Game/Blueprints/Character/Player/BP_Player")
if not bp:
    unreal.log_error("DIAG_ERROR=BP_Player load failed")
    raise RuntimeError("BP_Player load failed")

cdo = unreal.get_default_object(bp.generated_class())
components = cdo.get_components_by_class(unreal.PrimitiveComponent)
for component in components:
    path = component.get_path_name()
    profile = component.get_collision_profile_name()
    enabled = component.get_collision_enabled()
    object_type = component.get_collision_object_type()
    if player_channel is None:
        response = "ENUM_NOT_FOUND"
    else:
        response = component.get_collision_response_to_channel(player_channel)
    unreal.log_warning(
        f"PLAYER_COMPONENT path={path} profile={profile} enabled={enabled} "
        f"object_type={object_type} player_response={response}"
    )
