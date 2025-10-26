// Minimal stub for closed feature: provide encode_record used by GameScene.
// The real implementation is intentionally omitted from the public repo.
use super::GameScene;

/// Encode a record for upload. This is a stub that returns an empty payload.
/// Replace with the real implementation if/when available.
pub fn encode_record(_scene: &GameScene, _player_id: i32, _chart_id: i32) -> Vec<u8> {
    Vec::new()
}
